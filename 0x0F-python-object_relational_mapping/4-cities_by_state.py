#!/usr/bin/python3
import sys
import MySQLdb


if __name__ == "__main__":
    # arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect the SQL server
    db = MySQLdb.connect
    (host="localhost", port=3306, user=username, passwd=password, db=database)

    # Cursor Object to execute queries
    cursor = db.cursor()

    # SQL Query
    query = "SELECT * FROM cities ORDER BY id ASC"

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
