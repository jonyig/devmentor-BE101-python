# Event -ASSOCIATION - Route
# Event - DEPENDENCY - Visitor
from typing import List

from email import Email
from route import Route
from sms import Sms
from student import Student
from telegram import Telegram
from visitor import Visitor


class Event:
    event_name: str
    routes: List[Route] = []
    user: Visitor

    def __init__(self, event_name: str):
        self.event_name = event_name
        self.sms_route = Sms()
        self.email_route = Email()
        self.tg_route = Telegram()
        self.routes = []

    def add(self, route: Route):
        self.routes.append(route)

    def notify(self, user):
        self.user = user
        if self.event_name == "signup":
            self.notify_signup()
        elif self.event_name == "subscribe":
            self.notify_subscribe()
        elif self.event_name == "cancel":
            self.notify_cancel()

    def notify_signup(self):
        for route in self.routes:
            route.send(f" {self.user.name} signed up SUCCESSFULLY!")

    def notify_subscribe(self):
        for route in self.routes:
            route.send(f" {self.user.name} subscribed SUCCESSFULLY!")

    def notify_cancel(self):
        for route in self.routes:
            route.send(f" {self.user.name} cancelled SUCCESSFULLY!")
