#remainder for your need

# imports
from turtle import title
from win10toast import ToastNotifier #win10toast module
import time # for timer

toaster = ToastNotifier()

title = input("\nTitle of Remainder: ")
msg = input("Message: ")
minutes = float(input("How Many Minutes: "))

seconds = minutes * 15

print("\nRemainder Set Successfully!\n")
time.sleep(seconds)
toaster.show_toast(title, msg, duration=10, threaded=True)

while toaster.notification_active:
    time.sleep(0.1)
