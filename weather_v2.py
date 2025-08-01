import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
import datetime
from gtts import gTTS
import json

# Email settings from environment variables
EMAIL_SENDER = os.environ.get("EMAIL_SENDER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.environ.get("EMAIL_RECEIVER")
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))

# Load cities from JSON file
def load_cities_from_json(filename="Locations.json"):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            cities_data = json.load(f)
        print(f"Cities loaded from {filename}")
        return cities_data
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please create the JSON file with city data.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filename}. Please check the file format.")
        return {}

CITIES = load_cities_from_json()

def celsius_to_fahrenheit(celsius):
    """Converts Celsius temperature to Fahrenheit."""
    return (celsius * 9/5) + 32

def get_weather(city, lat, lon):
    """Fetch weather data for a city from Open-Meteo"""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp_celsius = data["current_weather"]["temperature"]
        temp_fahrenheit = celsius_to_fahrenheit(temp_celsius) # Convert to Fahrenheit
        weather_code = data["current_weather"]["weathercode"]
        description = weather_code_to_description(weather_code)
        return f"{city}: Temperature: {temp_celsius}°C ({temp_fahrenheit:.1f}°F), Condition: {description}"
    else:
        return f"{city}: Error fetching data (status code {response.status_code})"

def load_weather_codes(filename="weather_codes.json"):
    """Load weather codes from a JSON file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filename}.")
        return {}

WEATHER_CODES = load_weather_codes()

def weather_code_to_description(code):
    """Convert weather code to textual description"""
    return WEATHER_CODES.get(str(code), "Unknown ❓")

def send_email(weather_data, audio_file=None):
    """Send email with weather data and optional audio attachment"""
    if not all([EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER]):
        print("Error: Email credentials are not set. Please check your environment variables.")
        return

    subject = f"Weather Report - {datetime.date.today()}"
    body = "Today's weather report:\n\n" + "\n".join(weather_data)

    # Email setup with UTF-8 encoding
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = Header(subject, "utf-8").encode()
    msg.attach(MIMEText(body, "plain", "utf-8"))

    # Attach the audio file if it exists
    if audio_file and os.path.exists(audio_file):
        try:
            with open(audio_file, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(audio_file)}",
            )
            msg.attach(part)
            print(f"Attached audio file: {audio_file}")
        except Exception as e:
            print(f"Error attaching audio file: {e}")

    try:
        print("Connecting to SMTP server...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        print("Logging in to email server...")
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        print("Sending email...")
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Error sending email: SMTP Authentication Error. Please check your email and password. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while sending the email: {e}")

def main():
    """Main function to fetch and send weather data"""
    if not CITIES:
        print("No cities found to process. Exiting.")
        return

    weather_data = []
    for city, coords in CITIES.items():
        weather_info = get_weather(city, coords["lat"], coords["lon"])
        weather_data.append(weather_info)

    weather_report_text = "\n".join(weather_data)
    audio_file = generate_tts_audio(weather_report_text)
    
    send_email(weather_data, audio_file)

def generate_tts_audio(text, filename="weather_report.mp3"):
    """Generates TTS audio from text and saves it as an MP3 file."""
    try:
        print(f"Generating audio for: \"{text[:50]}...\"")
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(filename)
        print(f"Audio saved as {filename}")
        return filename
    except Exception as e:
        print(f"Error generating TTS audio: {e}")
        return None

if __name__ == "__main__":
    main()
