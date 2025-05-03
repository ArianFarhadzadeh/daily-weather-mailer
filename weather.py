import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import datetime

# Email settings

EMAIL_SENDER = os.environ["EMAIL_SENDER"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]
EMAIL_RECEIVER = os.environ["EMAIL_RECEIVER"]
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# City coordinates (lat, lon)
CITIES = {
    "Tehran": {"lat": 35.6892, "lon": 51.3890},
    "Mashhad": {"lat": 36.2970, "lon": 59.6057},
    "New York": {"lat": 40.7128, "lon": -74.0060},
    "Dallas": {"lat": 32.7767, "lon": -96.7970},
    "Houston": {"lat": 29.7604, "lon": -95.3698},
    "Austin": {"lat": 30.2672, "lon": -97.7431}
}

def get_weather(city, lat, lon):
    """Fetch weather data for a city from Open-Meteo"""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["current_weather"]["temperature"]
        weather_code = data["current_weather"]["weathercode"]
        description = weather_code_to_description(weather_code)
        return f"{city}: Temperature: {temp}°C, Condition: {description}"
    else:
        return f"{city}: Error fetching data (status code {response.status_code})"

def weather_code_to_description(code):
    """Convert weather code to textual description"""
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Fog and freezing",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Heavy drizzle",
        61: "Light rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Light snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Rain showers: light",
        81: "Rain showers: moderate",
        82: "Rain showers: violent",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Thunderstorm with heavy hail"
    }
    return weather_codes.get(code, "Unknown")

def send_email(weather_data):
    """Send email with weather information"""
    subject = f"Weather Report - {datetime.date.today()}"
    body = "Today's weather report:\n\n" + "\n".join(weather_data)

    # Email setup with UTF-8 encoding
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = Header(subject, "utf-8").encode()
    msg.attach(MIMEText(body, "plain", "utf-8"))

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
    weather_data = []
    for city, coords in CITIES.items():
        weather_info = get_weather(city, coords["lat"], coords["lon"])
        weather_data.append(weather_info)
    
    send_email(weather_data)

if __name__ == "__main__":
    main()
