# Event -ASSOCIATION - Route
# Event - DEPENDENCY - Visitor
from email import Email
from route import Route
from sms import Sms
from student import Student
from telegram import Telegram
from visitor import Visitor


class Event:
    event_name: str
    route: Route
    user: Visitor

    def __init__(self, event_name: str, user: Visitor = None):
        self.sms_route = Sms()
        self.email_route = Email()
        self.tg_route = Telegram()
        self.user = user

        if event_name == "signup":
            self.notify_signup()
            # print(f"Hello {visitor.name} just signed up!")
        elif event_name == "subscribe":
            self.notify_subscribe()
            # print("hello subscribe")
        elif event_name == "cancel":
            self.notify_cancel()
            # print("hello cancel")

    def notify_signup(self):
        self.sms_route.send(f" {self.user.name} signed up SUCCESSFULLY!")
        self.email_route.send(f" {self.user.name} signed up SUCCESSFULLY!")

    def notify_subscribe(self):
        self.email_route.send(f" {self.user.name} subscribed SUCCESSFULLY!")
        self.tg_route.send(f" {self.user.name} subscribed SUCCESSFULLY!")

    def notify_cancel(self):
        self.email_route.send(f" {self.user.name} cancelled SUCCESSFULLY!")
        self.tg_route.send(f" {self.user.name} cancelled SUCCESSFULLY!")
