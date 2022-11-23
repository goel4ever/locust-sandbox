# Locust Sandbox

Documentation for the project [here](./docs)

The examples in the project are safe to run as is.
Please do not run the examples with more than 5 users, else we may end up spamming some third party APIs.

## Running load test

```shell
$ locust -f basic_user_task.py

It'll start the web interface at http://localhost:8089 for further interaction
```

## On Start/Stop methods

```shell
Users and TaskSet has on_start() and on_stop() methods that execute only once.
These methods do not need @task annotation
Methods can be used to set up / clean up of test data or check for environments, etc.

$ locust -f basic_user_task.py

It'll start the web interface at http://localhost:8089 for further interaction
```

## Validating Response

Just because the response code is 200, doesn't mean the request is success.

```shell
Makes locust capture responses for the requests. Set in CRUD methods as parameter
catch_response=True

Within if condition, based on the validation logic, call either of the following
response.success()
response.failure()

Example:
with self.client.get("/json", catch_response=True, name="JSON") as response:
  if "SomeText" not in response.text or response.status_code != 200:
    response.failure("intentionally failing the request")
```

## Data Parameterization

Ways to parameterize data:

1. Test data in separate file
2. Test data in python file
3. Test data from third party library like [faker](https://faker.readthedocs.io/en/master/)

## Tagging

`@tag` is a decorator for tagging tasks and tasksets
Example: `@tag('get', 'json')`

Tags can be used to selectively run the test on tasks with specific tags.

```shell
$ locust -f locustfile.py --tags json
$ locust -f locustfile.py --exclude-tags get
```

## Correlation

Used for extracting dynamic values (via regular expressions or parsers) from the response, and passing the extracted value in the subsequent requests.

## Environment Variables

Ways to set up environment variables for locust

1. via command line
2. via environment variables like `LOCUST_HOST`, `LOCUST_USERS`, etc
3. `*.conf` file
4. `*.yaml` file

The options above are listed in the order of priority, in case properties are defined in multiple places.

Pass the custom config file with the flag `--config`

## References

> Note: Do not run heavy loads on third-party websites. These are only meant for verifying that the load test works.

- Official docs [Environment variables](https://docs.locust.io/en/stable/configuration.html#environment-variables)
- YT - QA Insights [Learn Locust Series](https://www.youtube.com/playlist?list=PLJ9A48W0kpRKMCzJARCObgJs3SinOewp5)
- Third-party APIs
  - [https://reqres.in/](https://reqres.in/)
  - [https://http.cat](https://http.cat)
  - [https://onlineboutique.dev](https://onlineboutique.dev)
- Third-party Tools
  - [faker](https://faker.readthedocs.io/en/master/)
  - [http://httpbin.org/](http://httpbin.org/)
  - [https://petstore.octoperf.com/](https://petstore.octoperf.com/)
