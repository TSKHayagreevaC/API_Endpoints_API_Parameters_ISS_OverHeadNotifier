# import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
#
# print(iss_position)

# if response.status_code != 404:
#     raise Exception("That Resource Does Not Exist.")
# elif response.status_code == 401:
#     raise Exception("You Are Not Authorised To Access This Data")

# Kanye Quotes Program

import requests

# from tkinter import *
# import requests
#
#
# def get_quote():
#     response = requests.get("https://api.kanye.rest")
#     response.raise_for_status()
#     data = response.json()
#     quote = data["quote"]
#     canvas.itemconfig(quote_text, text=quote)
#
#
# window = Tk()
# window.title("Kanye Quote Is ...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414) background_img = PhotoImage(file="background.png") canvas.create_image(150,
# 207, image=background_img) quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250,
# font=("Arial", 30, "bold"), fill="white") canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
# window.mainloop()

# SunRise And SunSet Time Display App...

import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "srikanthhayagreeva1993@gmail.com"
MY_PASSWORD = "*********"
MY_LAT = 28.484607
MY_LONG = 77.526068


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(120)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:LOOK AT ISS👆\n\nThe ISS is above you in the sky."
        )
