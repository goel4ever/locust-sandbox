from locust import task, HttpUser, constant, SequentialTaskSet


class MyHttpCatTask(SequentialTaskSet):
    """
    SequentialTaskSet is used to define tasks in sequential order
    All tasks are executed in an order (by default in the order tasks are defined)
    Note: Task weight attribute will be ignored in this case
    """

    @task
    def get_200_status(self):
        self.client.get("/200")
        print("get http status for 200")

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("get http status for 500")


class MyLoadTest(HttpUser):

    host = "https://http.cat"
    wait_time = constant(1)
    tasks = [MyHttpCatTask]
