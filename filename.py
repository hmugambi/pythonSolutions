import psycopg2
from psycopg2 import Error

class fileName:

    def __init__(self, filename):
        self.fileName = filename

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
    #database="postgres_db"

    usersFile = open("users.csv", "r")
    for line in usersFile:
        columns = line.split(",")
        #Name	Login	Email	Active
        cursor = connection.cursor()

        #  create users table
        #cursor.execute("CREATE TABLE users (name VARCHAR(255), Login VARCHAR(255), Email VARCHAR(255), Active VARCHAR(10) )")

        # insert into table
        sql = "INSERT INTO users (Name,Login,Email,Active) VALUES (%s, %s, %s, %s) "
        val = (columns[0], columns[1], columns[2], columns[3])

        cursor.execute(sql, val)
        connection.commit()

except (Exception, Error) as error:
    print("Error Encountered", error)
        print("PostgreSQL connection is closed")

else:
    print("Data Inserted successfully successfully in PostgreSQL ")
