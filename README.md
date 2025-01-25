# ISS Overhead Notification Program

This program notifies you via email when the International Space Station (ISS) is overhead and visible from your location. The ISS can only be seen when it is dark at your location and is within ±5 degrees latitude and longitude.

## Features
- Periodically checks the current position of the ISS using the [Open Notify ISS API](http://api.open-notify.org/iss-now.json).
- Verifies whether it's dark at your location using the [Sunrise-Sunset API](https://sunrise-sunset.org/api).
- Sends an email notification when the ISS is overhead and visible.
- Customizable configuration for user-specific variables.

---

## How It Works
1. Fetches the current location of the ISS.
2. Compares the ISS position with your location to see if it’s within ±5 degrees of latitude and longitude.
3. Since the ISS cannot be seen during the daytime, checks whether it’s dark at your location based on sunrise and sunset times.
4. If both conditions are met, sends a notification email to your configured email address.
5. Repeats the process every 60 seconds.

---

## Requirements
- Python 3.x
- Internet connection
- A Gmail account with [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) enabled
- The following Python libraries:
  - `requests`
  - `smtplib`
  - `datetime`
  - `time`

---

## Setup

1. Clone this repository or copy the code.
2. Install the required libraries (if not already installed):
   ```bash
   pip install requests
   ```
3. Create environment variables as needed, or a config.py file in the project directory with the following content:
   ```python
    # Replace these with your own values
    my_gmail = "your_email@gmail.com"
    app_pwd = "your_app_password"
    my_yahoo = "recipient_email@yahoo.com"
    MY_LAT = your_latitude # e.g., 37.7749
    MY_LONG = your_longitude # e.g., -122.4194
    tzid = "your_time_zone_id" # e.g., "America/Los_Angeles"
    formatted = 0 # Use 0 for 24-hour format, 1 for 12-hour format
    smtp_google = "smtp.gmail.com"
    port = 587

4. Run the script:
   ```bash
   python your_script_name.py
   ```
## Configuration Options
- ```MY_LAT``` and ```MY_LONG```: Specify your geographical latitude and longitude.
- ```tzid```: Your time zone identifier (e.g., "America/New_York").
- ```formatted```: Set to ```0``` for 24-hour time format or ```1``` for 12-hour time format.
- ```sleep_timer```: The interval (in seconds) to wait between checks. Default is ```60``` seconds.

## Important Notes
- Ensure the Gmail account used to send emails has **App Passwords** enabled.
- The recipient email address can be any valid email, not limited to Yahoo Mail.
- The program runs indefinitely, checking for the ISS every 60 seconds. You can terminate it manually (e.g., Ctrl+C).

## Troubleshooting
- No Email Received:
    - Check your config.py file for correct credentials.
    - Ensure App Passwords are enabled in your Gmail account.
    - Verify that the ISS is within range and it’s dark at your location.
  - API Errors:
    - Ensure you have an active internet connection.
    - Verify that the API endpoints (```api_iss``` and ```api_sunrise_sunset```) are accessible.

## Acknowledgments
- Open Notify ISS API for ISS location data.
- Sunrise-Sunset API for sunrise and sunset times.

## License
This project is licensed under the [GNU General Public Use v3 License](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Affiliation
This code is part of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" by Dr. Angela Yu and AppBrewery.