#  RemoteOK Job Scraper

This project is a Python-based web scraper that fetches remote job listings from the RemoteOK public API, saves the data into a PostgreSQL database, and exports it as a CSV file.  

---

##  Key Features

- Scrapes real-time job listings from RemoteOK API
- Stores job data in a PostgreSQL database
- Exports data to a timestamped CSV file
- Well-structured and easy-to-read code
- Prints jobs clearly in the terminal

---

##  Technologies Used

- Python 3
- Requests
- PostgreSQL
- Psycopg2
- Dotenv
- CSV
- RemoteOK API

---

##  Project Structure
RemoteOK_Scraper_Project/ ├── remote_jobs_scraper.py ├── .env ├── requirements.txt ├── remote_jobs_2025XXXX_XXXXXX.csv └── README.md

---

##  How to Run

1. Clone this repository:

git clone https://github.com/your-username/RemoteOK-Scraper.git cd RemoteOK-Scraper

2. Install required libraries:

pip install -r requirements.txt

3. Add your PostgreSQL connection URL in the .env file.

4. Run the scraper:

python remote_jobs_scraper.py

---

##  RemoteOK API

Jobs are fetched from: [https://remoteok.io/api](https://remoteok.io/api)

<<<<<<< HEAD
---
=======
---
>>>>>>> 1530d84db36c6fc5b99356e160c1568bae55c40a
