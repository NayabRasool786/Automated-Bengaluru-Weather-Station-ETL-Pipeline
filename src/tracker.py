import requests
import sqlite3
import os
import pandas as pd
from datetime import datetime

# --- CONFIGURATION ---
# Open-Meteo API URL
# We are asking for: Current Weather info including Temperature and Wind Speed
# Coordinates for Bengaluru City: Lat 12.9629, Long 77.5775
# To find YOUR coords: Right-click a place on Google Maps, the numbers are at the top.
LAT = "12.9629" 
LONG = "77.5775"
API_URL = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LONG}&current_weather=true"

DB_NAME = "data/bengaluru_weather_data.db"
CSV_NAME = "data/bengaluru_weather_data.csv"

def fetch_weather():
    """
    Hits the Open-Meteo API.
    """
    try:
        response = requests.get(API_URL)
        
        if response.status_code == 200:
            data = response.json()
            current_weather = data['current_weather']
            
            weather_data = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Temperature_C": current_weather['temperature'],
                "Wind_Speed_kmh": current_weather['windspeed'],
                "Is_Day": current_weather['is_day'] # 1 = Day, 0 = Night
            }
            return weather_data
        else:
            print(f"Error: Status code {response.status_code}")
            return None

    except Exception as e:
        print(f"Connection Error: {e}")
        return None
        

def save_to_dataFrame(data_dict):
    """
    Uses Pandas to append data. 
    1. Turn the single dictionary into a DataFrame (a mini-table).
    2. Append that mini-table to the CSV file.
    """
    # Create a DataFrame (A table with 1 row)
    df = pd.DataFrame([data_dict])
    
    # LOGIC: 
    # If file exists -> Append (mode='a') AND do not write headers (header=False)
    # If file does NOT exist -> Write (mode='w') AND write headers (header=True)
    
    if os.path.isfile(CSV_NAME):
        df.to_csv(CSV_NAME, mode='a', header=False, index=False)
    else:
        df.to_csv(CSV_NAME, mode='w', header=True, index=False)
        
    print(f"Pandas saved: {data_dict['Temperature_C']}°C")

def save_to_db(data):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create table (if not exists)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                temperature REAL,
                windspeed REAL,
                is_day INTEGER
            )
        ''')
        
        # timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute(
            "INSERT INTO weather_logs (timestamp, temperature, windspeed, is_day) VALUES (?, ?, ?, ?)",
            (data['Timestamp'], data['Temperature_C'], data['Wind_Speed_kmh'], data['Is_Day'])
        )
        
        conn.commit()
        conn.close()
        print(f"Logged to DB: {data['Temperature_C']}°C")
    except Exception as e:
        print(f"Database Error: {e}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print(f"--- Checking Weather for Lat: {LAT}, Long: {LONG} ---")
    weather_info = fetch_weather()
    
    if weather_info:
        save_to_dataFrame(weather_info)
        save_to_db(weather_info)
    else:
        print("Failed to get weather data.")
