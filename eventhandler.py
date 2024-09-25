from event import Event,RegisterEvent,CourseBookingEvent,CourseCancelEvent
from user import User

# EventHandler class
class EventHandler:
    def __init__(self,event_type, user: User):
        self.user = user
        self.event_type = event_type
        self.event_map = {
            "RegisterEvent": RegisterEvent(self.user),
            "CourseBookingEvent": CourseBookingEvent(self.user),
            "CourseCancelEvent": CourseCancelEvent(self.user)
        }

    def handle_event(self):
        if self.event_type in self.event_map.keys():
            event = self.event_map[self.event_type]
        else:
            print(f"No event found for {self.event_type}")
            raise ValueError(f"No event found for {self.event_type}")
        return event    
