# It is for basic Data Analysis

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load your specific CSV
csv_path = "data/bengaluru_weather_data.csv"

# Check if file exists first to avoid errors
import os
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)

    # 2. Convert 'Timestamp' column to proper Date format so Python understands time
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # 3. Plotting
    plt.figure(figsize=(10, 5)) # Make the chart wider
    plt.plot(df['Timestamp'], df['Temperature_C'], marker='o', linestyle='-', color='b')
    
    plt.title('Bengaluru Temperature Trend')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    print(f"Average Temp: {df['Temperature_C'].mean():.2f}°C")
    plt.show()
else:
    print("CSV file not found yet. Run the main script first!")
