import psycopg2

conn = psycopg2.connect(
    database='GreenhouseManager',
    user='postgres',
    password='Cwoodsdffc2010',
    host='localhost',
    port='5432'
)

conn.autocommit = True
cursor = conn.cursor

