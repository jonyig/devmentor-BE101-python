# This is a sample Python script.
from typing import List

from email import Email
from event import Event
from language import Language
from route import Route
from sms import Sms
from student import Student
from telegram import Telegram
from visitor import Visitor


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


    zhtw = Language("zh-tw")
    jonny = Visitor("jonny", zhtw)

    enus = Language("en-us")
    robert = Student("robert", enus)

    telegram = Telegram()
    email = Email()
    sms = Sms()
    print(robert.name)
    signupRoute: List[Route] = [sms, email]
    subscribeRoute: List[Route] = [email, telegram]
    cancelRoute: List[Route] = [email, telegram]
    signup = Event("signup")
    signup.notify(user=jonny, routes=signupRoute)
    subscribe = Event("subscribe")
    subscribe.notify(user=jonny, routes=subscribeRoute)
    cancel = Event("cancel")
    cancel.notify(user=jonny, routes=cancelRoute)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
