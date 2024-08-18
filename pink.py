
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://postgres:admin@localhost:5432/test')

query = '''
select * from main_post
'''
df = pd.read_sql_query(query, engine)
print(df)

