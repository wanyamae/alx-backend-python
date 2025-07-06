from seed import connect_to_prodev

def stream_user_ages():
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield int(row['age'])
    cursor.close()
    connection.close()

def average_age():
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    avg = total / count if count else 0
    print(f"Average age of users: {avg}")
