#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL Server
    db = MySQLdb.connect
    (host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL Query to fetch the states starting with N
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows returned by the Query
    rows = cursor.fetchall()

    # print the states in desired format
    for row in rows:
        print(rows)

    # close the cursor and database connection
    cursor.close()
    db.close()
