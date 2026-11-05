import sqlite3
conn=sqlite3.connect("battery.db")

# Initialize the database tables from the schema
with open("schema.sql", "r") as f:
    schema=f.read()
    
conn.executescript(schema)
conn.commit()
conn.close()