#%matplotlib inline
import os
import sys
import pandas as pd
import pymssql
import pandas.io.sql as psql
import matplotlib.pyplot as plt

cnxn = pymssql.connect(host='***',database='***',user='***',password='***')
sql = "***"
df = pd.read_sql(sql, cnxn)
cnxn.close()

qtd = df['mesanocompetencia'].value_counts()
qtd.plot(kind='barh', figsize=(20,5), grid=True, rot=0, color='blue', legend=False)
plt.title('Quantidade de atendimetos por mês em 2017')
plt.xlabel('Quantidade de atendimentos')
plt.show()