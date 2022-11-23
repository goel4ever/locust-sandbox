# Locust via Docker CLI

Running locust inside the docker container

```shell
$ docker run -p 8089:8089 -v $PWD:/mnt/locust \
  -d locustio/locust -f /mnt/locust/locustfile.py
```

Running locust inside the docker container (in headless mode)

```shell
$ docker run -v $PWD:/mnt/locust -d locustio/locust \
  -f /mnt/locust/locustfile.py --html /mnt/locust/myrun1.html \
  --headless --only-summary -r 1 -u 1 -t 10s
```

Accessing locust via shell

```shell
$ docker exec -it <container_id> /bin/bash
```
