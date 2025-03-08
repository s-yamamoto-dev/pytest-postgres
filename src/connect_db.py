import psycopg2

connection = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")

cursor = connection.cursor()
