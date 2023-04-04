FROM python:3.10-slim

ADD consumer.py .

RUN pip install --upgrade pip
RUN pip install confluent-kafka

CMD [ "python", "consumer.py" ]
