from locust import task, HttpUser, constant, TaskSet


class MyHttpCatTask(TaskSet):
    """
    TaskSets help structure the hierarchical navigation/paths
    TaskSet can be nested
    """

    @task
    def get_http_status(self):
        self.client.get("/200")
        print("get http status for 200")

        # Helps to come out of this class and go back to parent class, without any wait time
        # Setting reschedule=False allows wait time before sending the control back to parent class
        # reschedule is really meaning reschedule_immediately_or_not
        self.interrupt(reschedule=False)


class AnotherHttpCat(TaskSet):
    @task
    def get_500_status(self):
        self.client.get("/500")
        print("get status of 500")

        # Helps to come out of this class and go back to parent class, without any wait time
        # Setting reschedule=False allows wait time before sending the control back to parent class
        # reschedule is really meaning reschedule_immediately_or_not
        self.interrupt(reschedule=False)


class MyLoadTest(HttpUser):

    host = "https://http.cat"
    wait_time = constant(1)
    # Note: for 1 user, it'll pick one of the class and stick to it
    # to change this, you need interrupt in both the classes
    tasks = [MyHttpCatTask, AnotherHttpCat]
