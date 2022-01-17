import smtplib
import time
import os
import sys

os.system("cls")

for char in "Welcome to the Email Sender.":
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
time.sleep(2)

for char in "\nMutayyab is not responsible for how I use the program.":
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)

for char in "\nPress any key to agree and continue...":
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.005)
input()

os.system("cls")

senderEmail = input("Enter your email: ")
password = input("Enter Password: ")
recieverEmails = input("Enter a user you would like to send an email to: ")
message = input("Enter a message to send to the users: ")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(senderEmail, password)
print("Logged in...")

for recieverEmail in recieverEmails:
    try:
        server.sendmail(senderEmail, recieverEmail, message)
        print(f"The email has been sent to {recieverEmail}!")
    except Exception as e:
        print("An error occured!", e)