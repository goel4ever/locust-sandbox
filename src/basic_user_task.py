from locust import User, task


class MyTestUser(User):
    def on_start(self):
        print("Starting...")

    @task
    def launch(self):
        print("Launching the URL")

    @task
    def search(self):
        print("Searching")

    def on_stop(self):
        print("Stopping...")


if __name__ == '__main__':
    MyTestUser.search()
