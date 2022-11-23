import logging

from locust import task, events, SequentialTaskSet, HttpUser, constant


@events.spawning_complete.add_listener
def spawn_users(user_count, **kwargs):
    print("spawned ... {} users.".format(user_count))


@events.request_success.add_listener
def send_notification(**kwargs):
    print("Sending the success notification")


@events.request_failure.add_listener
def send_notification(**kwargs):
    print("Sending the failure notification")


@events.quitting.add_listener
def sla(environment, **kwargs):
    if environment.stats.total.fail_ratio > 0.01:
        logging.error("Test failed due to failure ratio > 0.01%")
        environment.process_exit_code = 1
        print(environment.process_exit_code)
    else:
        environment.process_exit_code = 0
        print(environment.process_exit_code)


class LoadTest(SequentialTaskSet):

    @task
    def home_page(self):
        self.client.get("/", name="T01_SuccessRequests")
        self.client.get("/failed", name="T02_FailedRequests")


class TestScenario(HttpUser):
    host = "https://onlineboutique.dev"
    wait_time = constant(1)
    tasks = [LoadTest]

    def on_start(self):
        print("Starting...")

    def on_stop(self):
        print("Stopping...")
