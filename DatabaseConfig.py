import psycopg2
from requests import options

conn = psycopg2.connect(
    database='GreenhouseManager',
    user='postgres',
    password='Cwoodfc2010',
    host='localhost',
    port='5432',
    sslmode='disable'
)

cursor = conn.cursor

