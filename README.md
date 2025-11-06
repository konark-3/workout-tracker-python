# Workout Tracker with Nutritionix & Sheety

This Python script allows you to **log your daily exercises** and automatically track them in a Google Sheet. It uses the **Nutritionix API** to calculate exercise details like duration and calories burned, and logs them via **Sheety API**.

---

## Tech Stack

- **Language:** Python 3.x  
- **Libraries:** `requests`, `datetime`, `os`  
- **APIs:** 
  - Nutritionix API (for parsing exercises and calculating calories)  
  - Sheety API (for logging exercises in Google Sheets)  
- **Other tools:** Environment variables for storing API credentials securely  

---

## Features

- Accepts natural language input for exercises (e.g., "Ran 2 miles and walked 3 km").  
- Calculates:
  - Exercise type
  - Duration (minutes)
  - Calories burned  
- Logs exercise details automatically into a Google Sheet.  
- Records date and time of each workout entry.  

---

## Requirements

- Python 3.x  
- Packages:
  - `requests`  

Install dependencies using pip:

`pip install requests`

## Setup

Configure environment variables:

### Run:

`python main.py`

## Outcome
-------

-   Fetches exercise data via Nutritionix API

-   Logs date, time, duration, and calories to Google Sheet via Sheety API

-   Uses environment variables for secure authentication
