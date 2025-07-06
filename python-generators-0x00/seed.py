def insert_sample_data(connection, data):
    cursor = connection.cursor()
    for row in data:
        cursor.execute(
            """INSERT IGNORE INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)""",
            (row['user_id'], row['name'], row['email'], row['age'])
        )
    connection.commit()
    cursor.close()
    print("Sample data inserted successfully")

import mysql.connector

def connect_db():
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



if __name__ == "__main__":
    connection = connect_db()
    if connection:
        create_database(connection)
        connection.close()
        print("connection successful")

        connection = connect_to_prodev()
        if connection:
            create_table(connection)
            sample_data = [
                {"user_id": "11111111-1111-1111-1111-111111111111", "name": "Johnnie Mayer", "email": "Ross.Reynolds21@hotmail.com", "age": 35},
                {"user_id": "22222222-2222-2222-2222-222222222222", "name": "Myrtle Waters", "email": "Edmund_Funk@gmail.com", "age": 99},
                {"user_id": "33333333-3333-3333-3333-333333333333", "name": "Flora Rodriguez I", "email": "Willie.Bogisich@gmail.com", "age": 84},
                {"user_id": "44444444-4444-4444-4444-444444444444", "name": "Dr. Cecilia Konopelski-Lakin", "email": "Felicia75@gmail.com", "age": 87},
                {"user_id": "55555555-5555-5555-5555-555555555555", "name": "Chelsea Boyle-Stoltenberg", "email": "Regina.Emard97@yahoo.com", "age": 83},
                {"user_id": "66666666-6666-6666-6666-666666666666", "name": "Seth Mraz", "email": "Cecilia_Blanda89@gmail.com", "age": 24},
                {"user_id": "77777777-7777-7777-7777-777777777777", "name": "Thelma Kris-Schinner", "email": "Johnnie.Jast93@hotmail.com", "age": 6},
                {"user_id": "88888888-8888-8888-8888-888888888888", "name": "Thomas Hane", "email": "Dominic24@yahoo.com", "age": 93},
                {"user_id": "99999999-9999-9999-9999-999999999999", "name": "Della Hickle", "email": "Leon_Rohan@hotmail.com", "age": 35},
                {"user_id": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa", "name": "Kristi Durgan", "email": "Maria_Schmeler9@hotmail.com", "age": 70}
            ]
            insert_sample_data(connection, sample_data)