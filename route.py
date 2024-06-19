# Route -REALIZATION- TG,SMS,Email
from abc import ABC, abstractmethod


class Route(ABC):
    @abstractmethod
    def send(self, msg):
        return msg