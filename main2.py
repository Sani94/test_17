import psycopg2
import pandas as pd

conn = psycopg2.connect(host="localhost",dbname="test",user="postgres",password="admin",port=5432)


cur = conn.cursor()

sql = cur.execute("""SELECT * FROM main_post""")



for row in cur.fetchall():
    df = pd.DataFrame(row)



conn.commit()

cur.close()
conn.close()


