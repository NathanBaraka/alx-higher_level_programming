#!/usr/bin/python3
"""This module lists all states from the hbtn_0e_0_usa database."""
import sys
import MySQLdb

if __name__ == "__main__":
    # Gets the MySQL credentials from command-line args.
    # Connects to MySQL server.
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Executing the SQL query to retrieve all states sorted by id.
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
