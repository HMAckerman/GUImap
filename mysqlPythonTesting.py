from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'pythonSQL'

config = {
    'user': 'root',
    'password': 'Taekwondo1$',
    'host': '127.0.0.1',
    'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
# Creates a database and then shows it! The cursor function executes a SQL
# statement.
# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE DATABASE pythonSQL")
#
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#     print(x)
#
# mydb.close()


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8mb4'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)
