from locust import task, HttpUser, constant
from locust.event import EventHook

send_email_notifications = EventHook()
send_text_notifications = EventHook()


def email(i, j, req_id, message=None, **kwargs):
    print("Sending {} in the email for the request {}.".format(message, req_id))


def sms_text(i, j, req_id, message=None, **kwargs):
    print("Sending {} in the SMS for the request {}.".format(message, req_id))


send_email_notifications.add_listener(email)
send_text_notifications.add_listener(sms_text)


class LoadTest(HttpUser):
    host = "https://onlineboutique.dev"
    wait_time = constant(1)

    def on_start(self):
        print("Starting...")

    def on_stop(self):
        print("Stopping...")

    @task
    def home_page(self):
        with self.client.get("/", name="T00_HomePage", catch_response=True) as response:
            if response.status_code == 200:
                send_email_notifications.fire(i=1, j=2, req_id=1, message="success")
                send_text_notifications.fire(i=1, j=2, req_id=2, message="success")
            else:
                send_email_notifications.fire(i=1, j=2, req_id=1, message="failure")
                send_text_notifications.fire(i=1, j=2, req_id=2, message="failure")

        with self.client.get("/test", name="T01_FailedHomePage", catch_response=True) as response:
            if response.status_code == 200:
                send_email_notifications.fire(i=1, j=2, req_id=3, message="success")
                send_text_notifications.fire(i=1, j=2, req_id=4, message="success")
            else:
                send_email_notifications.fire(i=1, j=2, req_id=3, message="failure")
                send_text_notifications.fire(i=1, j=2, req_id=4, message="failure")
