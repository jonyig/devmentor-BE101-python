# Event -ASSOCIATION - Route
# Event - DEPENDENCY - Visitor
class Event:
    def notify(self,visitor):
        print(f"Notify {visitor}")