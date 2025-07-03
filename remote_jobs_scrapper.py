# fetch_and_store.py

import requests
import csv
from db import get_connection

# Step 1: Fetch data
url = "https://remoteok.io/api"
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    exit()

data = response.json()
jobs = data[1:]

# Step 2: Save to CSV
csv_file = "remote_jobs.csv"
with open(csv_file, "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Company", "Position", "Location", "Tags", "Apply Link"])

    for job in jobs:
        company = job.get("company", "N/A")
        position = job.get("position", "N/A")
        location = job.get("location", "Remote")
        tags = ", ".join(job.get("tags", []))
        apply_link = job.get("url", "N/A")

        writer.writerow([company, position, location, tags, apply_link])

print(f"CSV file '{csv_file}' generated successfully.")

# Step 3: Insert into DB
try:
    conn, cursor = get_connection()
    print("Connected to the database.")

    for job in jobs:
        company = job.get("company", "N/A")
        position = job.get("position", "N/A")
        location = job.get("location", "Remote")
        tags = ", ".join(job.get("tags", []))
        apply_link = job.get("url", "N/A")

        cursor.execute("""
            INSERT INTO remote_jobs (company, position, location, tags, apply_link)
            VALUES (%s, %s, %s, %s, %s);
        """, (company, position, location, tags, apply_link))

    conn.commit()
    print(f"{len(jobs)} job(s) inserted into the database.")

except Exception as e:
    print("Error inserting into database:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Database connection closed.")
