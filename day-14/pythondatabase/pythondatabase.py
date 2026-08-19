
import sqlite3

# ==========================================
# 1. DATABASE CONNECTION
# ==========================================

connection = sqlite3.connect("hotel.db")
cursor = connection.cursor()

print("Database connected successfully!")


# ==========================================
# 2. CREATE TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS rooms (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    guest_name TEXT NOT NULL,
    room_number INTEGER UNIQUE NOT NULL,
    room_type TEXT,
    price REAL
)
""")

print("Table created successfully!")


# ==========================================
# 3. INSERT MULTIPLE RECORDS
# ==========================================

guests = [
    ("Rahul", 101, "Single", 1500),
    ("Aman", 102, "Double", 2500),
    ("Priya", 103, "Deluxe", 3500),
    ("Neha", 104, "Suite", 5000)
]

cursor.executemany("""
INSERT INTO rooms
(guest_name, room_number, room_type, price)
VALUES (?, ?, ?, ?)
""", guests)

connection.commit()

print("Multiple records inserted successfully!")


# ==========================================
# 4. FETCH ALL RECORDS
# ==========================================

cursor.execute("SELECT * FROM rooms")

all_rooms = cursor.fetchall()

print("\n----- ALL HOTEL RECORDS -----")

for room in all_rooms:
    print(room)


# ==========================================
# 5. FETCH ONE RECORD
# ==========================================

cursor.execute("""
SELECT * FROM rooms
WHERE room_id = ?
""", (1,))

one_room = cursor.fetchone()

print("\n----- ONE HOTEL RECORD -----")
print(one_room)


# ==========================================
# 6. UPDATE RECORD
# ==========================================

cursor.execute("""
UPDATE rooms
SET price = ?
WHERE room_id = ?
""", (2000, 1))

connection.commit()

print("\nRoom record updated successfully!")


# Check updated record

cursor.execute("""
SELECT * FROM rooms
WHERE room_id = ?
""", (1,))

updated_room = cursor.fetchone()

print("Updated record:")
print(updated_room)


# ==========================================
# 7. DELETE RECORD
# ==========================================

cursor.execute("""
DELETE FROM rooms
WHERE room_id = ?
""", (4,))

connection.commit()

print("\nRoom record deleted successfully!")


# ==========================================
# 8. FETCH ALL RECORDS AFTER DELETE
# ==========================================

cursor.execute("SELECT * FROM rooms")

remaining_rooms = cursor.fetchall()

print("\n----- RECORDS AFTER DELETE -----")

for room in remaining_rooms:
    print(room)


# ==========================================
# 9. CLOSE DATABASE CONNECTION
# ==========================================

connection.close()

print("\nDatabase connection closed!")

