FROM python:3.10-slim

ADD producer.py .

RUN pip install --upgrade pip
RUN pip install requests
RUN pip install confluent-kafka
RUN pip install pytz

CMD [ "python", "producer.py" ]
