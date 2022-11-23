import json
from locust import task, HttpUser, constant


class MyTestUser(HttpUser):
    """
    HttpUser creates a client (instance of HttpSession)
    `self.client` is the instance
    """

    host = "https://reqres.in"

    # default wait time is in seconds
    wait_time = constant(1)

    @task
    def get_users(self):
        resp = self.client.get("/api/users?page=2")
        print(resp.text)
        print(resp.status_code)
        print(resp.headers)

    @task
    def create_user(self):
        payload = {
            "name": "some name",
            "job": "leader",
        }
        resp = self.client.post("/api/users", data=json.dumps(payload))
        print(resp.text)
        print(resp.status_code)
        print(resp.headers)
