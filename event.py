# Event -ASSOCIATION - Route
# Event - DEPENDENCY - Visitor
from typing import List

from email import Email
from route import Route
from sms import Sms
from telegram import Telegram
from visitor import Visitor


class Event:
    event_name: str
    routes: List[Route] = []
    user: Visitor

    def __init__(self, event_name: str):
        self.event_name = event_name
        self.routes = []

    def add(self, route: Route):
        self.routes.append(route)

    def notify(self, user):
        self.user = user
        sentenceMap = {
            "signup": "signed up SUCCESSFULLY!",
            "subscribe": "subscribed SUCCESSFULLY!",
            "cancel": "cancelled SUCCESSFULLY!",
        }

        sentence: str = sentenceMap[self.event_name]

        for route in self.routes:
            route.send(f" {self.user.name} {sentence}")
