# User class
class User:
    def __init__(self, id: str, email: str, phone: str, prefers_language: str):

        self.id = id
        self.email = email
        self.phone = phone
        self.prefers_language = prefers_language

    def register(self):
        return "RegisterEvent"

    def course_booking(self):
        return "CourseBookingEvent"

    def course_cancel(self):
        return "CourseCancelEvent"
