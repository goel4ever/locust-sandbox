import random
import re

from locust import SequentialTaskSet, task, HttpUser, constant


class PetStore(SequentialTaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.jsession = ""
        self.random_product = ""

    @task
    def home_page(self):
        with self.client.get("", catch_response=True, name="T00_HomePage") as response:
            if "Welcome to JPetStore 6" in response.text and response.elapsed.total_seconds() < 2.0:
                response.success()
            else:
                response.failure("Home page took too long to load or text check has failed")

    @task
    def enter_store(self):
        products = ["Fish", "Dogs", "Cats", "Reptiles", "Birds"]
        with self.client.get("/actions/Catalog.action", catch_response=True, name="T10_EnterStore") as response:
            for product in products:
                if product in response.text:
                    response.success()
                else:
                    response.failure("Product check failed")

            try:
                jsession = re.search(r"jsessionid=(.+?)\?", response.text)
                self.jsession = jsession.group(1)
            except AttributeError:
                self.jsession = ""

    @task
    def signin_page(self):
        self.client.cookies.clear()
        url = "/actions/Account.action;jsessionid={}?signonForm=".format(self.jsession)
        with self.client.get(url, catch_response=True, name="T20_SignInPage") as response:
            if "Please enter your username and password." in response.text:
                response.success()
            else:
                response.failure("Sign in page check failed")
                # print(response.text)

    @task
    def login_page(self):
        self.client.cookies.clear()
        url = "/actions/Account.action"
        data = {
            "username": "j2ee",
            "password": "j2ee",
            "signon": "Login",
        }
        with self.client.post(url, catch_response=True, name="T30_SignIn", data=data) as response:
            if "Welcome ABC!" in response.text:
                response.success()
                try:
                    random_product = re.findall(r"Catalog.action\?viewCategory=&categoryId=(.+?)\"", response.text)
                    self.random_product = random.choice(random_product)
                except AttributeError:
                    self.random_product = ""
            else:
                response.failure("Sign in failed")

    @task
    def random_product_page(self):
        url = "/actions/Catalog.action?viewCategory=&categoryId={}".format(self.random_product)
        page_name = "T40_{}_Page".format(self.random_product)
        with self.client.get(url, catch_response=True, name=page_name) as response:
            if self.random_product in response.text:
                response.success()
            else:
                response.failure("Product page not loaded")

    @task
    def sign_out(self):
        url = "/actions/Account.action?signoff="
        with self.client.get(url, catch_response=True, name="T50_SignOff") as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to log off")

        self.client.cookies.clear()


class LoadTest(HttpUser):
    host = "https://petstore.octoperf.com"
    wait_time = constant(1)
    tasks = [PetStore]
