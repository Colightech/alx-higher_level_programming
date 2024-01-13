#!/usr/bin/python3
"""a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa:"""
import MySQLdb
import sys

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", user=sys.argv[1], password=sys.argv[2],
    db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for roe in rows:
        print(row)
    cur.close()
    conn.close()
