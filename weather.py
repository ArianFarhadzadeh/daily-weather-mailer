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
import json # Added this line

# Email settings
EMAIL_SENDER = os.environ["EMAIL_SENDER"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]
EMAIL_RECEIVER = os.environ["EMAIL_RECEIVER"]
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

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

CITIES = load_cities_from_json() # Calling the function to load cities

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

def weather_code_to_description(code):
    """Convert weather code to textual description"""
    # Some WMO Weather Codes (WMO4677)
    # https://epic.awi.de/id/eprint/29966/1/WMO2011h.pdf
    weather_codes = {
        0: "Clear sky ☀️",
        1: "Mainly clear 🌤️",
        2: "Partly cloudy ⛅",
        3: "Overcast ☁️",
        45: "Fog 🌫️",
        48: "Fog and freezing ❄️🌫️",
        51: "Drizzle, light 🌧️",
        53: "Drizzle, moderate 🌧️",
        55: "Drizzle, heavy 🌧️",
        61: "Rain, light ☔",
        63: "Rain, moderate ☔",
        65: "Rain, heavy ☔",
        71: "Snow, light 🌨️",
        73: "Snow, moderate 🌨️",
        75: "Snow, heavy 🌨️",
        80: "Rain showers, light 🌧️",
        81: "Rain showers, moderate 🌧️",
        82: "Rain showers, heavy ⛈️",
        95: "Thunderstorm ⚡⛈️",
        96: "Thunderstorm with hail ⚡🌨️🧊",
        99: "Thunderstorm with heavy hail ⚡🌨️🧊"
    }
    return weather_codes.get(code, "Unknown ❓")

def send_email(weather_data, audio_file=None):
    """Send email with weather data and optional audio attachment"""
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
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    """Main function to fetch and send weather data"""
    if not CITIES: # Added this condition to check if CITIES is empty
        print("No cities found to process. Exiting.")
        return

    weather_data = []
    for city, coords in CITIES.items():
        weather_info = get_weather(city, coords["lat"], coords["lon"])
        weather_data.append(weather_info)

    weather_report_text = "\n".join(weather_data)
    audio_file = generate_tts_audio(weather_report_text)
    
    # Pass both weather_data (for email body) and audio_file (for attachment)
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
