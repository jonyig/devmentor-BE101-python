# This is a sample Python script.
from typing import List

from email import Email
from en_us import Enus
from event import Event
from language import Language
from route import Route
from sms import Sms
from student import Student
from telegram import Telegram
from visitor import Visitor
from zh_tw import Zhtw


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    zhtw = Zhtw()
    enus = Enus()
    print(zhtw.get_msg(msg_key="signup"))
    print(enus.get_msg(msg_key="signup"))

    jonny = Visitor("jonny", zhtw)

    telegram = Telegram()
    email = Email()
    sms = Sms()

    signup = Event("signup")
    signup.add(sms)
    signup.add(email)
    signup.notify(user=jonny)

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
