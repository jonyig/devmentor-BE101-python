# This is a sample Python script.
from typing import List

from email import Email
from event import Event
from language import Language
from sms import Sms
from student import Student
from telegram import Telegram
from visitor import Visitor



# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    zhtw = Language(lang_code="zhtw")
    enus = Language(lang_code="enus")
    jonny = Visitor(name="jonny", language=zhtw)
    robert = Student(name="robert", language=enus)

    telegram = Telegram()
    email = Email()
    sms = Sms()

    signup = Event("signup")
    signup.add(sms)
    signup.add(email)
    signup.notify(user=robert)

    subscribe = Event("subscribe")
    subscribe.add(email)
    subscribe.add(telegram)
    subscribe.notify(user=jonny)

    cancel = Event("cancel")
    cancel.add(email)
    cancel.add(telegram)
    cancel.notify(user=jonny)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
