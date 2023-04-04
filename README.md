# tpiuo
repozitorij laboratorijskih vježbi iz vještine Tehnologije podatkovnog inženjerstva u oblaku

**Ime:** Josip

**Prezime:** Arelić

**Email:** josip.arelic@fer.hr

### Upute za pokretanje

pokrenuti kafka servise i topic:
	-u /kafka pokrenuti naredbu
    ```sh
    docker-compose up -d
	```
    ```sh
    docker exec kafka-kafka1-1 kafka-topics --bootstrap-server kafka-kafka1-1:9092 --create --partitions 3 --topic ethereum
    ```

stvoriti docker slike:
	-u /producer pokrenuti naredbu 
    ```sh
    docker build -t python-kafka-producer .
	```
    -u /consumer pokrenuti naredbu 
    ```sh
    docker build -t python-kafka-consumer .
    ```

zatim pokrenuti preostale producer i composer kontejnere
	```sh
    docker run --name python-producer-container --network kafka_kafka_network -dit python-kafka-producer
	```
    ```sh
    docker run --name python-consumer-container --network kafka_kafka_network -dit python-kafka-consumer
    ```

stanje kafka servisa također se može pratiti na http://localhost:8080