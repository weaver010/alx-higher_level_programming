#!/usr/bin/python3
"""script should take 4 arguments: mysql username,
mysql password, database name and
state name searched (safe from MySQL injection)"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (sys.argv[4],))
    s = c.fetchall()
    for i in s:
        print(i)
