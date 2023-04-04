from datetime import datetime, date, time
from time import sleep
from pytz import UTC
from confluent_kafka import Producer
import requests

url = 'http://api.coincap.io/v2/assets/ethereum/history'

conf = {'bootstrap.servers': 'kafka1:19092'}
producer = Producer(conf)

def extractFromApi():
    # today midnight(00:00) in epoch miliseconds
    today_ms = int(datetime.combine(date.today(), time(0,0,0,0), UTC).timestamp() * 1000)
    # hundred days before
    htoday_ms = today_ms - 100 * (24 * 60 * 60 * 1000)
    # seventy days before
    stoday_ms = today_ms - 70 * (24 * 60 * 60 * 1000)
    # forty days before
    ftoday_ms = today_ms - 40 * (24 * 60 * 60 * 1000)
    # ten days before
    ttoday_ms = today_ms - 10 * (24 * 60 * 60 * 1000)
    
    print(htoday_ms)
    print(stoday_ms)
    print(ftoday_ms)
    print(ttoday_ms)
    print(today_ms)
    
    # because max day difference is 30 (api.coincap), possible refactoring
    payload1 = {'interval': 'h1', 'start': htoday_ms, 'end': stoday_ms} # 100 - 70
    payload2 = {'interval': 'h1', 'start': stoday_ms, 'end': ftoday_ms} # 70 - 40
    payload3 = {'interval': 'h1', 'start': ftoday_ms, 'end': ttoday_ms} # 40 - 10
    payload4 = {'interval': 'h1', 'start': ttoday_ms, 'end': today_ms} # 10 - 0
    
    # no records for some days, for example 01/01/2023
    r = requests.get(url, params=payload1)
    data = r.json()['data']
    
    print(len(data))
    
    r = requests.get(url, params=payload2)
    data.extend(r.json()['data'])
    
    print(len(data))
    
    r = requests.get(url, params=payload3)
    data.extend(r.json()['data'])
    
    print(len(data))
    
    r = requests.get(url, params=payload4)
    data.extend(r.json()['data'])
    
    print(len(data))
    return data

if __name__ == '__main__':
    
    data = extractFromApi()
    
    cleaned_data = []
    for item in data:
        cleaned_data.append({'priceUsd': item['priceUsd'], 'time': item['time']})
    
    k = 0
    
    for item in cleaned_data:
        v = str(item['time']) + ',' + str(item['priceUsd'])
        print(str(k) + " " + v)
        
        producer.produce('ethereum', key=str(k).encode(), value=v)
        sleep(0.1)
        k += 1
    
    producer.flush()
    