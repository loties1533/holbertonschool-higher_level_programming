#!/usr/bin/python3
"""
script qui liste tout les states (états) de la base de données hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":


    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    """
    tous les states(états) par 'id' ordre croissant
    """
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
