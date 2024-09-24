from abc import ABC, abstractmethod

# Event Interface
class Event(ABC):
    @abstractmethod
    def add_channel(self, notification: Notification):
        """
        Every event should have an add_channel method
        """
        pass

    @abstractmethod
    def notify(self, user: User):
        """
        Every event should have a notify method
        """
        pass


# RegisterEvent
class RegisterEvent(Event):
    def __init__(self):
        self.content = {"zh-TW": "註冊成功", "en-US": "Registration Successful"}
        self.channels = [Email(), SMS()]

    def add_channel(self, notification: Notification):
        self.channels.append(notification)

    def notify(self, user: User):
        message = self.content.get(user.prefers_language, "Registration Successful")
        for channel in self.channels:
            channel.send_message(message, user)


# CourseBookingEvent
class CourseBookingEvent(Event):
    def __init__(self):
        self.content = {"zh-TW": "學生預約課程成功", "en-US": "Course Booking Successful"}
        self.channels = [Email(), Telegram()]

    def add_channel(self, notification: Notification):
        self.channels.append(notification)

    def notify(self, user: User):
        message = self.content.get(user.prefers_language, "Course Booking Successful")
        for channel in self.channels:
            channel.send_message(message, user)


# CourseCancelEvent
class CourseCancelEvent(Event):
    def __init__(self):
        self.content = {"zh-TW": "學生取消課程", "en-US": "Course Cancellation"}
        self.channels = [Email(), Telegram()]

    def add_channel(self, notification: Notification):
        self.channels.append(notification)

    def notify(self, user: User):
        message = self.content.get(user.prefers_language, "Course Cancellation")
        for channel in self.channels:
            channel.send_message(message, user)
