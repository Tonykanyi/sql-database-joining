#!/usr/bin/env python
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='myduka_db' user='postgres' host='localhost' password='Tony41943318'")
except:
    print("I am unable to connect to the database")

cur= conn.cursor()
cur.execute("select *from products;")
rows=cur.fetchall()
print(rows)