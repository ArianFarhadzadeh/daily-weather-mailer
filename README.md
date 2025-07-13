# ☁️ Weather Report Emailer

This Python script fetches current weather information for predefined cities using the [Open-Meteo API](https://open-meteo.com/) and sends a daily weather report via email.

---

## 📜 Table of Contents

* [✨ Features](#-features)
* [🚀 Setup](#-setup)
* [🏃‍♀️ How to Run](#️-how-to-run)
* [🛠️ Troubleshooting](#️-troubleshooting)
* [🤝 Contributing](#-contributing)

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

Before running the script, ensure you have **Python** installed. You'll also need to install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Environment Variables for Security

This script uses environment variables to securely handle sensitive information like your email credentials. This ensures your private data is not exposed in the codebase, especially when sharing your project publicly.

You need to set the following environment variables before running the script:

*   `EMAIL_SENDER`: Your Gmail address (e.g., `your.email@gmail.com`)
*   `EMAIL_PASSWORD`: Your Gmail App password (this is not your regular Gmail password)
*   `EMAIL_RECEIVER`: The recipient's email address (e.g., `recipient.email@example.com`)

Rename `env.sh.template` to `env.sh` (for Linux/macOS) or `env.bat.template` to `env.bat` (for Windows) and add your settings to `env.sh` or `env.bat.  **Do not commit your actual credentials to the *.template files.**


### Customizing Cities via JSON

Instead of hardcoding cities in the Python script, you can now manage your city list using a `locations.json` file. This allows for easy addition, modification, or removal of cities without changing the main script.

Create a file named `locations.json` (get inspiration from the template file `locations.json.template`)  in the same directory as `weather.py` and populate it with your desired cities and their coordinates.

---

## 🏃‍♀️ How to Run

After setting up the prerequisites, configuring your environment variables, and creating your `Locations.json` file, you can run the script from your terminal:

```bash
python weather.py
```

Upon successful execution, you should see "Email sent successfully." in your terminal, and the recipient will receive the weather report email with an audio attachment.

---

## 🛠️ Troubleshooting

*   **Error sending email: Authentication failed:** Double-check your `EMAIL_SENDER` and `EMAIL_PASSWORD` environment variables.
*   **KeyError: 'EMAIL_SENDER'**: This means the environment variables weren't set correctly.
*   **Error fetching data (status code XXX):** Check your internet connection and the Open-Meteo API status.
*   **Email not received:** Check the recipient's spam folder.
*   **Error: Locations.json not found or could not be decoded:** Ensure the file exists and contains valid JSON.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
