import smtplib
import json
import datetime as dt
import random as rd
import pandas as pd
import os

with open("credentials.json", "r") as file:
    data = json.load(file)

my_email = data["Email"]
my_password = data["Password"]

def send_quote(recipient_name, recipient_email, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:Happy birthday {recipient_name}!\n\n{message}")

templates =[open(os.path.join("letter_templates",template)).read() for template in os.listdir("letter_templates")]

birthdays = pd.read_csv("birthdays.csv")

for index, row in birthdays.iterrows():
    if row["month"] == dt.datetime.now().month and row["day"] == dt.datetime.now().day:
        name = row["name"]
        email = row["email"]
        message = rd.choice(templates).replace("[NAME]", name)
        send_quote(name,email,message)




