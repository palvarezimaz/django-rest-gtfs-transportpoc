"""
A quick script that populates GTFS data into a pre-defined PostgreSQL database.
"""
import os
import csv
import psycopg2


host = 'localhost'
dbname = 'transportpoc'
user = 'user'
password = '123qwe'

conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
cur = conn.cursor()
gtfs_directory = '../sources/schedule'


for file in os.listdir(gtfs_directory): # Loop through each file and get filename as table
    if file.endswith('.txt'):
        table_name = os.path.splitext(file)[0]  # remove extension
        file_path = os.path.join(gtfs_directory, file)

        # read header for column names
        with open(file_path, 'r', encoding='utf-8') as gtfs_file:
            reader = csv.reader(gtfs_file, delimiter=',')
            header_row = next(reader)
            columns = []
            for col_name in header_row:
                columns.append(f"{col_name} TEXT")  # Treating all data as TEXT

            table_columns = ", ".join(columns)

        cur.execute(f"CREATE TABLE {table_name} (id SERIAL PRIMARY KEY, {table_columns})")
        conn.commit()

        # Feed data to the table
        with open(file_path, 'r', encoding='utf-8') as gtfs_file:
            reader = csv.reader(gtfs_file, delimiter=',')
            next(reader)  # Skip the header row
            for row in reader:
                cur.execute(f"INSERT INTO {table_name} ({','.join(header_row)}) VALUES ({','.join(['%s']*len(header_row))})", row)
            conn.commit()

cur.close()
conn.close()