---

# Weather Report Emailer

This Python script fetches current weather information for predefined cities using the Open-Meteo API and sends a daily weather report via email.

## Features

* Fetches **current temperature and weather conditions** for multiple cities.
* Converts **weather codes to human-readable descriptions**.
* Sends a formatted **email** containing the weather report.
* **Customizable city list** for weather inquiries.

## Setup

### Prerequisites

Before running the script, ensure you have Python installed. You'll also need to install the `requests` library:

```bash
pip install requests
```

### Gmail App Password

To send emails using a Gmail account, you need to generate an **App password**. This is more secure than using your regular Gmail password directly in the script.

1.  Go to your Google Account.
2.  Navigate to **Security**.
3.  Under "How you sign in to Google," select **2-Step Verification**. You might need to sign in.
4.  Scroll down to "App passwords" and click on it.
5.  Follow the instructions to generate a new app password. Make sure to **copy this password immediately** as you won't be able to see it again.

### Configuration

Open the `your_script_name.py` file and modify the following variables in the **Email settings** section:

* `EMAIL_SENDER`: Your Gmail address.
* `EMAIL_PASSWORD`: The **App password** you generated (not your regular Gmail password).
* `EMAIL_RECEIVER`: The recipient's email address.

You can also customize the `CITIES` dictionary to add or remove cities by providing their `latitude` and `longitude`.

```python
# Email settings
EMAIL_SENDER = "your.email@gmail.com"  # Sender's email
EMAIL_PASSWORD = "your_gmail_app_password"  # Gmail app password
EMAIL_RECEIVER = "recipient.email@example.com"  # Receiver's email

# City coordinates (lat, lon)
CITIES = {
    "Tehran": {"lat": 35.6892, "lon": 51.3890},
    "London": {"lat": 51.5074, "lon": -0.1278},
    # Add or remove cities as needed
}
```

## How to Run

After setting up the prerequisites and configuration, you can run the script from your terminal:

```bash
python your_script_name.py
```

Upon successful execution, you should see "Email sent successfully." in your terminal, and the recipient will receive the weather report email.

## Troubleshooting

* **"Error sending email: Authentication failed"**: Double-check `EMAIL_SENDER` and `EMAIL_PASSWORD`. Ensure you are using the **App password** and not your regular Gmail password. Also, confirm that 2-Step Verification is enabled for your Gmail account.
* **"Error fetching data (status code XXX)"**: This indicates an issue with the API request. Check your internet connection and ensure the `Open-Meteo` API is accessible.
* **Email not received**: Check the recipient's spam folder. Ensure `EMAIL_RECEIVER` is correct.

---

Feel free to contribute to this project by suggesting improvements or adding new features!
