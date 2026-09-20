import smtplib
import json

with open("credentials.json", "r") as file:
    data = json.load(file)

my_email = data["Email"]
my_password = data["Password"]

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user = my_email, password = my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="a.radtschenko@yandex.ru",
        msg="Subject:Very importatnt mail\n\nNa?!?!? Geht's schon? ")
