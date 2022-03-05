import sqlalchemy
import csv
import sqlite3
import pandas as pd
from sqlalchemy import create_engine

database = 'testDB'
db_ext = '.db'
scan_database = database + db_ext
file_name = 'scanresults'
csv_ext = '.csv'
# csv_file = file_name + csv_ext
csv_file = 'test_scan.csv'

engine = create_engine(f'sqlite:///{scan_database}', echo = True)
conn = sqlite3.connect(scan_database)

scan_data = pd.read_csv(csv_file)
scan_data.to_sql('nmap', conn, if_exists='replace', index=False)

cur = conn.cursor()

for row in cur.execute('SELECT * FROM nmap'):
    print(row)
conn.close()