#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    
    # Create a cursor object to execute queries
    cursor = db.cursor()
    
    # Create the SQL query using the user input
    query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(state_name)
    
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