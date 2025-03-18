import sqlite3
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    action TEXT NOT NULL,
    timestamp TEXT NOT NULL
)
""")
conn.commit()

def register_entry(name, action):
    """ Register entry or exit in the database """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO attendance (name, action, timestamp) VALUES (?, ?, ?)", (name, action, timestamp))
    conn.commit()
    print(f"✅ {name} {action} recorded at {timestamp}.")

def show_records():
    """ Display all attendance records """
    cursor.execute("SELECT * FROM attendance")
    records = cursor.fetchall()
    
    if not records:
        print("ℹ️ No records found.")
    else:
        print("\n📋 Attendance Records:")
        for record in records:
            print(f"🆔 {record[0]} | 👤 {record[1]} | 🔄 {record[2]} | ⏰ {record[3]}")

# Main menu
while True:
    print("\n🎯 Attendance Management System")
    print("1️⃣ Register Entry")
    print("2️⃣ Register Exit")
    print("3️⃣ Show All Records")
    print("4️⃣ Exit")

    choice = input("👉 Enter your choice: ")

    if choice == "1":
        name = input("👤 Enter name: ")
        register_entry(name, "Entry")
    elif choice == "2":
        name = input("👤 Enter name: ")
        register_entry(name, "Exit")
    elif choice == "3":
        show_records()
    elif choice == "4":
        print("👋 Exiting the program.")
        break
    else:
        print("⚠️ Invalid choice! Please try again.")

# Close database connection
conn.close()
