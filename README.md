# ☁️ Weather Report Emailer

This Python script fetches current weather information for predefined cities using the [Open-Meteo API](https://open-meteo.com/) and sends a daily weather report via email.

---

## ✨ Features

* Fetches **current temperature and weather conditions** for multiple cities.
* Converts **weather codes to human-readable descriptions**.
* Sends a formatted **email** containing the weather report.
* **Customizable city list** for weather inquiries.

---

## 🚀 Setup

### Prerequisites

Before running the script, ensure you have **Python** installed. You'll also need to install the `requests` library, which is used to make API calls:

```bash
pip install requests
```

### Environment Variables for Security

This script uses **environment variables** to securely handle sensitive information like your email credentials. This ensures your private data is not exposed in the codebase, especially when sharing your project publicly.

You need to set the following environment variables before running the script:

* `EMAIL_SENDER`: Your Gmail address (e.g., `your.email@gmail.com`)
* `EMAIL_PASSWORD`: Your Gmail **App password** (this is ***not*** your regular Gmail password)
* `EMAIL_RECEIVER`: The recipient's email address (e.g., `recipient.email@example.com`)

This you can do by edit `env.bat` for Windows, `env.sh` for Linux.

And then run the batch file from the command line.

**Note!** For Linux you need to make it executable first, `chmod +x env.sh`.

#### Generating a Gmail App Password:

If you don't have an App password, follow these steps:

1.  Go to your [Google Account Security page](https://myaccount.google.com/security).
2.  Under "How you sign in to Google," select **2-Step Verification**. If it's not enabled, you'll need to enable it first. You might need to sign in again.
3.  Scroll down to "**App passwords**" and click on it.
4.  Follow the instructions to generate a new app password. Make sure to **copy this password immediately** as you won't be able to see it again.

#### Setting Environment Variables (Before Running the Script):

**For Linux/macOS (Bash/Zsh terminal):**

Edit `env.sh`

```bash
export EMAIL_SENDER="your.email@gmail.com"
export EMAIL_PASSWORD="your_gmail_app_password" # Use the generated App Password
export EMAIL_RECEIVER="recipient.email@example.com"
```

**For Windows (Command Prompt):**

Edit `env.bat`

```cmd
set EMAIL_SENDER="your.email@gmail.com"
set EMAIL_PASSWORD="your_gmail_app_password"
set EMAIL_RECEIVER="recipient.email@example.com"
```

**For Windows (PowerShell):**

```powershell
$env:EMAIL_SENDER="your.email@gmail.com"
$env:EMAIL_PASSWORD="your_gmail_app_password"
$env:EMAIL_RECEIVER="recipient.email@example.com"
```

**Note:** These environment variables will only be active for the current terminal session. If you close the terminal or open a new one, you'll need to set them again.

### Customizing Cities

You can customize the `CITIES` dictionary directly in your Python script (e.g., `main.py`) to add or remove cities by providing their `latitude` and `longitude`. You can find city coordinates using various online tools.

```python
# City coordinates (lat, lon)
CITIES = {
    "Tehran": {"lat": 35.6892, "lon": 51.3890},
    "New York": {"lat": 40.7128, "lon": -74.0060},
    # Add or remove cities as needed
}
```

---

## 🏃‍♀️ How to Run

After setting up the prerequisites and configuring your environment variables, you can run the script from your terminal:

```bash
python main.py
```

Upon successful execution, you should see `"Email sent successfully."` in your terminal, and the recipient will receive the weather report email.

---

## 🛠️ Troubleshooting

* **`Error sending email: Authentication failed`**:
    * Double-check your `EMAIL_SENDER` and `EMAIL_PASSWORD` environment variables. Ensure you're using the **App password** for `EMAIL_PASSWORD` and not your regular Gmail password.
    * Confirm that **2-Step Verification** is enabled for your Gmail account.
* **`KeyError: 'EMAIL_SENDER'` (or `EMAIL_PASSWORD`, `EMAIL_RECEIVER`)**:
    * This means the environment variables weren't set correctly before running the script. Review the "Setting Environment Variables" section.
* **`Error fetching data (status code XXX)`**:
    * This indicates an issue with the API request. Check your internet connection.
    * Ensure the `Open-Meteo` API is accessible (sometimes temporary service issues can occur).
* **Email not received**:
    * Check the recipient's spam or junk folder.
    * Ensure the `EMAIL_RECEIVER` environment variable is correct.

---

Feel free to contribute to this project by suggesting improvements or adding new features!
