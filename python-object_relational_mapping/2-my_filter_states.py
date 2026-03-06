#!/usr/bin/python3
"""
script qui affiche tout les states (états) de la table 'states'
de la base de données hbtn_0e_0_usa
le nom correspond à l'argument (sys.argv[4]) passé en parametre
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    query = """SELECT *
                FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(state_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
