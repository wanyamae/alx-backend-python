import mysql.connector

def connect_db():
    # Connect to MySQL server (not a specific database)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1896'
    )
    return connection

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    cursor.close()

def connect_to_prodev():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1896',
        database='ALX_prodev'
    )
    return connection

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX(user_id)
        );
    """)
    cursor.close()
    print("Table user_data created successfully")

# Insert data from CSV if not already present
import csv
import os

def insert_data(connection, csv_file):
    if not os.path.exists(csv_file):
        print(f"{csv_file} not found.")
        return

    cursor = connection.cursor()
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute("""
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (row['user_id'], row['name'], row['email'], row['age']))
    connection.commit()
    cursor.close()
    print("Data inserted successfully")