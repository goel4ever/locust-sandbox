from locust import User, constant, task


class MyFirstUser(User):
    """
    `weight` defines the probability of picking up this class
    `wait_time` adds pause between operations
    In this example, we're distributing the probability 50% among the two classes
    Remember: The test needs to have at least 2 users, otherwise only one of the classes will run
    """
    weight = 2
    wait_time = constant(1)

    @task
    def launch(self):
        print("Launching the first URL")

    @task
    def search(self):
        print("Searching first")


class MySecondUser(User):
    weight = 2
    wait_time = constant(1)

    @task
    def launch(self):
        print("Launching the second URL")

    @task
    def search(self):
        print("Searching second")
