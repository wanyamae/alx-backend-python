import mysql.connector
from seed import connect_to_prodev


def streamusersinbatches(batchsize):
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    batch = []
    for row in cursor:
        batch.append(row)
        if len(batch) == batchsize:
            yield batch
            batch = []
    if batch:
        yield batch
    cursor.close()
    connection.close()

def batch_processing(batchsize):
    for batch in streamusersinbatches(batchsize):
        for user in batch:
            if int(user['age']) > 25:
                print(user)
