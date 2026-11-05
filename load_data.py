import sqlite3
import csv
from tkinter import INSERT
conn = sqlite3.connect("battery.db")

# Read battery records from CSV and load them into the database
with open("battery.csv", "r") as f:
    reader = csv.reader(f)
    header=next(reader)
    sql = "INSERT OR REPLACE INTO battery_cycles VALUES(?, ?, ?, ?, ?, ?)"
    conn.executemany(sql, reader)
    
conn.commit()
conn.close()