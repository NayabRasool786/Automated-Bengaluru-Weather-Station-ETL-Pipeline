# 🌤️ Automated Weather ETL Pipeline

A Python-based **ETL (Extract, Transform, Load)** pipeline that tracks real-time weather data for a specific location. It automatically fetches data from the Open-Meteo API, processes it using Pandas, and persists it into both a SQLite database and a CSV dataset for historical analysis.

![Alt text](data/Automated-Weather-Station-ETL-Pipeline.png.png)

## 📂 Project Structure

This project is designed to be modular and scalable.

```bash
weather-tracker/
│
├── data/                   # Stores the output files
│   ├── bengaluru_weather_data.csv # Flat file storage for quick analysis
│   └── bengaluru_weather_data.db  # SQLite database for structured querying
│
├── src/                    # Source code
│   └── tracker.py          # Main ETL script
│
├── analysis/               # (Optional) Analysis scripts
│   └── plot_data.py        # Visualizes trends using Matplotlib
│
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

```

## 🚀 Features

* **Extract:** Fetches real-time weather (Temperature, Wind Speed, Day/Night status) via the **Open-Meteo API** (No API key required).
* **Transform:** Uses **Pandas** to structure raw JSON into a clean DataFrame format, handling timestamps and data types.
* **Load:**
* **SQLite:** Appends data to a local relational database for persistent storage.
* **CSV:** Maintains a parallel flat-file log for easy integration with Excel or visualization tools.


* **Scalable:** Designed to run on a schedule (Cron Job or Windows Task Scheduler) for 24/7 monitoring.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Libraries:** `pandas`, `requests`, `sqlite3`, `datetime`, `os`
* **API:** [Open-Meteo](https://open-meteo.com/)

## ⚙️ Setup & Installation

1. **Clone the Repository**
```bash
git clone https://github.com/NayabRasool786/Automated-Bengaluru-Weather-Station-ETL-Pipeline.git
cd weather-tracker

```


2. **Install Dependencies**
It is recommended to use a virtual environment.
```bash
pip install pandas requests

```


*(Note: `sqlite3`, `os`, and `datetime` are part of the Python standard library.)*
3. **Configure Location**
Open `src/tracker.py` and update the `LAT` and `LONG` constants for your target city (Default: Bengaluru).
```python
LAT = "12.9629"
LONG = "77.5775"

```



## 🏃‍♂️ Usage

**Manual Run:**
To fetch the current weather and save it once:

```bash
python src/tracker.py

```

*Check the `data/` folder to see the generated `.csv` and `.db` files.*

**Automated Run (Scheduled):**
To build a dataset over time, automate the script to run every hour.

* **Windows (Task Scheduler):**
* Create a basic task -> Trigger: "Daily" -> Repeat task every: "1 hour".
* Action: Start a program -> `python.exe` -> Argument: `path\to\src\tracker.py`.


* **Linux/Mac (Cron Job):**
* Run `crontab -e` and add:
```bash
0 * * * * /usr/bin/python3 /path/to/weather-tracker/src/tracker.py

```





## 📊 Sample Data Output

**CSV Format:**

```csv
Timestamp,Temperature_C,Wind_Speed_kmh,Is_Day
2023-10-27 14:00:00,28.5,12.0,1
2023-10-27 15:00:00,27.8,11.5,1

```
---

## 🔗 Connect with Me
👋 Hi, I'm **NAYAB RASOOL SHAIK**

[![🔗LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/nayabrasool-shaik)  
[![Email](https://img.shields.io/badge/Email-Send%20Mail-blue?logo=gmail)](mailto:nayabshaik046@example.com)  
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-blueviolet?logo=google-chrome)](http://nayabrasool.my.canva.site/)

> _“Learn deeply, build practically, explain simply, and share widely.” – Shaik Nayab Rasool_

