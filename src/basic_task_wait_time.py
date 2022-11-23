import json
import time

from locust import User, task, constant_pacing


class MyTestUser(User):
    """
    By default, wait_time is in seconds
    1. constant(seconds)
    2. between(min, max)
    3. constant_pacing(seconds)
    4. constant_throughput(seconds)
    """

    wait_time = constant_pacing(5)

    @task
    def launch_with_pace(self):
        time.sleep(3)
        # Because constant_pacing is set to 5 seconds
        # If it takes too much time to complete the task, then constant_pacing will be zero
        print("Total execution time is 3 seconds, but it will wait for 5 seconds")

    @task
    def launch_no_pace(self):
        time.sleep(8)
        # constant_pacing is not applied since the tasks takes more time than the constant_pacing value
        # The task still completes in 8 sec, but locust will not wait for the task to complete and spawning a new test
        print("Total execution time is 8 seconds, even if wait is 5 seconds")
