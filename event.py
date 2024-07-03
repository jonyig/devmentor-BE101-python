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

    def __init__(self, event_name: str):
        self.event_name = event_name
        self.sms_route = Sms()
        self.email_route = Email()
        self.tg_route = Telegram()
        self.routes = [self.sms_route, self.email_route, self.tg_route]

    def notify(self, user, routes: List[Route]):
        self.user = user
        if self.event_name == "signup":
            self.notify_signup(routes)
        elif self.event_name == "subscribe":
            self.notify_subscribe(routes)
        elif self.event_name == "cancel":
            self.notify_cancel(routes)

    def notify_signup(self, routes: List[Route]):
        for route in routes:
            route.send(f" {self.user.name} signed up SUCCESSFULLY!")
        # self.sms_route.send(f" {self.user.name} signed up SUCCESSFULLY!")
        # self.email_route.send(f" {self.user.name} signed up SUCCESSFULLY!")

    def notify_subscribe(self, routes: List[Route]):
        for route in routes:
            route.send(f" {self.user.name} subscribed SUCCESSFULLY!")
        # self.email_route.send(f" {self.user.name} subscribed SUCCESSFULLY!")
        # self.tg_route.send(f" {self.user.name} subscribed SUCCESSFULLY!")

    def notify_cancel(self, routes: List[Route]):
        for route in routes:
            route.send(f" {self.user.name} cancelled SUCCESSFULLY!")
        # self.email_route.send(f" {self.user.name} cancelled SUCCESSFULLY!")
        # self.tg_route.send(f" {self.user.name} cancelled SUCCESSFULLY!")
