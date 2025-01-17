import time
import requests
from datetime import datetime
import smtplib
import config # configuration file for user specific variables

# user configured items
sender_email = config.my_gmail
sender_app_pwd = config.app_pwd
recipient_email = config.my_yahoo
user_lat = config.MY_LAT
user_long = config.MY_LONG
user_tzid = config.tzid
user_formatted_param = config.formatted
sleep_timer = 60

# API URLs
api_iss = "http://api.open-notify.org/iss-now.json"
api_sunrise_sunset = "https://api.sunrise-sunset.org/json"

# function to send notification from sender email to recipient email
def send_notification_email():
    with smtplib.SMTP(config.smtp_google, config.port) as connection:
        connection.starttls()
        connection.login(sender_email, sender_app_pwd)
        connection.sendmail(sender_email, recipient_email, "Subject: Look up!\n\nThe ISS is overhead!")
    print("Message sent")

# get the current ISS location from its API
def get_iss_current_location():
    response = requests.get(url=api_iss)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return {
        "iss_lat": iss_latitude,
        "iss_lng": iss_longitude
    }

# determine if ISS is within +/- 5 degrees latitude and longitude from user's location
def is_iss_close():
    iss_loc = get_iss_current_location()
    print(f"Current ISS location: {iss_loc['iss_lat']}, {iss_loc['iss_lng']}")
    print(f"Your location: {user_lat}, {user_long}")
    return (abs(user_lat - iss_loc['iss_lat']) <= 5
            and abs(user_long - iss_loc['iss_lng']) <= 5)

# check if it is currently dark using the sunrise-sunset time API
# ISS can be spotted in the sky only when it is dark
def is_it_dark():
    parameters = {
        "lat": user_lat,
        "lng": user_long,
        "tzid": user_tzid,
        "formatted": user_formatted_param,
    }

    response = requests.get(api_sunrise_sunset, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = int(str(time_now).split(" ")[1].split(":")[0])

    return hour_now <= sunrise or hour_now >= sunset


# Your position is within +5 or -5 degrees of the ISS position.
# If the ISS is close to my current position and it is currently dark
# Then send me an email to tell me to look up.
def look_for_iss():
    if is_iss_close() and is_it_dark():
        print("Look up")
        # send email
        send_notification_email()
    # Optional elif and else blocks, can be deleted if not needed
    elif not is_it_dark():
        print("It's overhead, but it's too bright to see it")
    else:
        print("It's too far")

# Run code every 60 seconds.
while True:
    look_for_iss()
    time.sleep(sleep_timer)