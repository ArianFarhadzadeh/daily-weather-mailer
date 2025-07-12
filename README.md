# ☁️ Weather Report Emailer

This Python script fetches current weather information for predefined cities using the [Open-Meteo API](https://open-meteo.com/) and sends a daily weather report via email.

---

## ✨ Features

* Fetches **current temperature and weather conditions** for multiple cities.
* Converts **weather codes to human-readable descriptions**.
* Sends a formatted **email** containing the weather report.
* **Customizable city list** for weather inquiries, now configurable via a JSON file.
* Generates an **audio summary** of the weather report and attaches it to the email.

---

## 🚀 Setup

### Prerequisites

Before running the script, ensure you have **Python** installed. You'll also need to install the `requests` and `gTTS` libraries, which are used to make API calls and generate audio respectively:

```bash
pip install requests gtts
Environment Variables for Security
This script uses environment variables to securely handle sensitive information like your email credentials. This ensures your private data is not exposed in the codebase, especially when sharing your project publicly.
```
You need to set the following environment variables before running the script:

EMAIL_SENDER: Your Gmail address (e.g., your.email@gmail.com)

EMAIL_PASSWORD: Your Gmail App password (this is not your regular Gmail password)

EMAIL_RECEIVER: The recipient's email address (e.g., recipient.email@example.com)

Setting Environment Variables (Before Running the Script):
You can use the provided env.sh (for Linux/macOS) or env.bat (for Windows) as templates. Do not commit your actual credentials to these files. Instead, you can:

Copy the template: Create a new file (e.g., my_env.sh or my_env.bat) from the template.

Edit the copy: Add your credentials to this new file.

Source the file (Linux/macOS): Before running the script, execute source my_env.sh in your terminal.

Run the batch file (Windows): Before running the script, execute my_env.bat in your command prompt.

Ensure the copied file is in your .gitignore to prevent accidental commits.

Alternatively, you can set the environment variables directly in your terminal session:

Set environments in Linux/macOS (Bash/Zsh terminal):
Bash

export EMAIL_SENDER="your.email@gmail.com"
export EMAIL_PASSWORD="your_gmail_app_password" # Use the generated App Password
export EMAIL_RECEIVER="recipient.email@example.com"
Set environments in Windows (Command Prompt):
DOS

set EMAIL_SENDER="your.email@gmail.com"
set EMAIL_PASSWORD="your_gmail_app_password"
set EMAIL_RECEIVER="recipient.email@example.com"
Set environments in Windows (PowerShell):
PowerShell

$env:EMAIL_SENDER="your.email@gmail.com"
$env:EMAIL_PASSWORD="your_gmail_app_password"
$env:EMAIL_RECEIVER="recipient.email@example.com"
Note: These environment variables will only be active for the current terminal session. If you close the terminal or open a new one, you'll need to set them again.

To make the environment variables persistent:
https://www.howtogeek.com/787217/how-to-edit-environment-variables-on-windows-10-or-11/

https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/

Generating a Gmail App Password:
If you don't have an App password, follow these steps:

Go to your Google Account Security page.

Under "How you sign in to Google," select 2-Step Verification. If it's not enabled, you'll need to enable it first. You might need to sign in again.

Scroll down to "App passwords" and click on it.

Follow the instructions to generate a new app password. Make sure to copy this password immediately as you won't be able to see it again.

Customizing Cities via JSON
Instead of hardcoding cities in the Python script, you can now manage your city list using a Locations.json file. This allows for easy addition, modification, or removal of cities without changing the main script.

Create a file named Locations.json in the same directory as weather2.py (or your main script).

Populate Locations.json with your desired cities and their coordinates in the following format:

JSON

{
    "Tehran-IR": {"lat": 35.6892, "lon": 51.3890},
    "Mashhad-IR": {"lat": 36.2970, "lon": 59.6057},
    "New York-USA": {"lat": 40.7128, "lon": -74.0060},
    "Dallas-USA": {"lat": 32.7767, "lon": -96.7970},
    "Houston-USA": {"lat": 29.7604, "lon": -95.3698},
    "Austin-USA": {"lat": 30.2672, "lon": -97.7431},
    "Bochum-DE" : {"lat":51.45972109228949,"lon": 7.234279823365569}
    // Add or remove cities as needed
}
Ensure the JSON file is correctly formatted. If the file is not found or has an invalid format, the script will print an error and exit.

🏃‍♀️ How to Run
After setting up the prerequisites, configuring your environment variables, and creating your Locations.json file, you can run the script from your terminal:

Bash

python weather2.py
Upon successful execution, you should see "Email sent successfully." in your terminal, and the recipient will receive the weather report email with an audio attachment.

🛠️ Troubleshooting
Error sending email: Authentication failed:

Double-check your EMAIL_SENDER and EMAIL_PASSWORD environment variables. Ensure you're using the App password for EMAIL_PASSWORD and not your regular Gmail password.

Confirm that 2-Step Verification is enabled for your Gmail account.

KeyError: 'EMAIL_SENDER' (or EMAIL_PASSWORD, EMAIL_RECEIVER):

This means the environment variables weren't set correctly before running the script. Review the "Setting Environment Variables" section.

Error fetching data (status code XXX):

This indicates an issue with the API request. Check your internet connection.

Ensure the Open-Meteo API is accessible (sometimes temporary service issues can occur).

Email not received:

Check the recipient's spam or junk folder.

Ensure the EMAIL_RECEIVER environment variable is correct.

Error: Locations.json not found or Error: Could not decode JSON from Locations.json:

Ensure Locations.json exists in the same directory as weather2.py and that its content is valid JSON.

Feel free to contribute to this project by suggesting improvements or adding new features!
