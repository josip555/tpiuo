# tpiuo
repozitorij laboratorijskih vježbi iz vještine Tehnologije podatkovnog inženjerstva u oblaku

**Ime:** Josip

**Prezime:** Arelić

**Email:** josip.arelic@fer.hr

#### Upute za pokretanje

Pokrenuti kafka servise i topic:

	U /kafka pokrenuti naredbu

    ```
    docker-compose up -d
	```

    ```
    docker exec kafka-kafka1-1 kafka-topics --bootstrap-server kafka-kafka1-1:9092 --create --partitions 3 --topic ethereum
    ```

Stvoriti docker slike:

	U /producer pokrenuti naredbu

    ```
    docker build -t python-kafka-producer .
	```

    U /consumer pokrenuti naredbu

    ```
    docker build -t python-kafka-consumer .
    ```

Zatim pokrenuti preostale producer i composer kontejnere:

	```
    docker run --name python-producer-container --network kafka_kafka_network -dit python-kafka-producer
	```

    ```
    docker run --name python-consumer-container --network kafka_kafka_network -dit python-kafka-consumer
    ```

Stanje kafka servisa također se može pratiti na http://localhost:8080 .