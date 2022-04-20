import os
import psycopg2

conn = psycopg2.connect(
    database='GreenhouseManager',
    user=os.environ['postgres'],
    password=os.environ['Cwoodfc2010'],
    host='localhost',
    port='5432'
)

conn.autocommit = True
cursor = conn.cursor

