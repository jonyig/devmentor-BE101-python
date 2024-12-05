from typing import List

from route import Route
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

        for route in self.routes:
            route.send(f" {self.user.name} {self.user.language.get_msg(self.event_name)}")