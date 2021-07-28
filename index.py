import pyautogui
import time
import os
import ctypes
def slowtype(strings):
    for letter in strings:
        print(letter, end="", flush=True)
        time.sleep(0.06)
ctypes.windll.kernel32.SetConsoleTitleW("Discord Spammer By Dank Rainbow")
slowtype("Welcome to my Discord Spammer")
print("\n")
time.sleep(1)
slowtype("Clearing in 2 seconds")
print("\n")
time.sleep(1)
slowtype("Clearing in 1 second")
print("\n")
time.sleep(1)
slowtype("Clearing...")
time.sleep(0.25)
os.system("cls")

msg = input("Message to spam?")

slowtype("You have untill this countdown finishes (5 Seconds) to put your cursor on the place you want to spam")

print("\n")
print("5")
time.sleep(1)
print("\n")
print("4")
time.sleep(1)
print("\n")
print("3")
time.sleep(1)
print("\n")
print("2")
time.sleep(1)
print("\n")
print("1")
print("\n")
print("Times Up. sending now.")

for i in range(100):
    pyautogui.write(msg)
    pyautogui.press("ENTER")
    print("message sent")
    time.sleep(3)
