# Event -ASSOCIATION - Route
# Event - DEPENDENCY - Visitor
class Event:
    def notify(self,visitor):
        print(f"Notify {visitor}")

    def __init__(self, event_name: str):
        if event_name == "signup":
            print("Hello signup")
        elif event_name == "subscribe":
            print("hello subscribe")
        elif event_name == "cancel":
            print("hello cancel")

    # def signup(self):
    #     self.notify()
    #     return
    #
    # def subscribe(self):
    #     return
    #
    # def cancel(self):
    #     return