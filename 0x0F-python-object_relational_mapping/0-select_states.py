#!/usr/bin/python3
"""This module lists all states from the mySQL database"""
import sys
import MySQLdb

def list_states (username, password, database):
    """The lists all the states from the database hbtn_0e_0_usa.
    args:
        username: mysql username
        password: mysql password
        database: mysql database
    """
    # Connecting to the MySQL server.
    db = MySQLdb.connect(host='localhost',\
            port=3306,\
            user=username,\
            passwd=password,\
            db=database)
    cursor = db.cursor()

    # Executing the SQL query to fetch all states.
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetching all the rows from the query result
    rows = cursor.fetchall()

    # Printing the results.
    for row in rows:
        print(row)

    # Closing the database connection.
    db.close()

# Example usage
if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
