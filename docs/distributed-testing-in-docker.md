# Distributed Load Testing in Docker

To run multiple containers, we can leverage docker compose.

## docker-compose.yaml

```yaml
version: '3'

services:
  master:
    image: locustio/locust
    ports:
      - "8089:8089"
    volumes:
      - ./:/mnt/locust
    command: -f /mnt/locust/locustfile.py --master --expect-workers 2

  worker1:
    image: locustio/locust
    volumes:
      - ./:/mnt/locust
    command: -f /mnt/locust/locustfile.py --worker --master-host master

  worker2:
    image: locustio/locust
    volumes:
      - ./:/mnt/locust
    command: -f /mnt/locust/locustfile.py --worker --master-host master
```

## Starting the test

```shell
$ docker-compose up
```