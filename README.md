# Weather Streaming Pipeline with Kafka and Docker
This is the result of a University Project for the course "Project: Data Engineering". The task was to create a simple data system, that streams data via Kafka. The system is supposed to be hosted in Docker containers.

## Instructions
Go to https://openweathermap.org/api and sign up for the free account to get your free API key. Then change the API key in the producer.py file in the variable "api_url".
There are two docker compose files because of Kafkas start-up time. Even with a depency configuration in the docker compose file the prodcuer and conumer containers will not wait long enough and create errors.
Therefore, first run "docker-compose_sep_main.yaml" and then "docker-compose_sep.yaml" via the appropriate docker compose command.

To connect to mongo-express open any webbrowser and access it via "http://localhost:8081/" with username: admin and password: pass

## Overview
6 Containers in total:
- Kafka
- MongoDB
- Mongo-Express
- Kafka Producer Python script
- Kafka Consumer Python script weather
- Kafka Consumer Python script location
