#!/usr/bin/python3
'''Selec states'''


if __name__ == '__main__':
    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
