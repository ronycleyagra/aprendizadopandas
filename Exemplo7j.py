#%matplotlib inline
import os
import sys
import pandas as pd
import pymssql
import pandas.io.sql as psql
import matplotlib.pyplot as plt
import configuraion as conf
import querys

cnxn = pymssql.connect(host=conf.host,database=conf.daabase,user=conf.user,password=condf.password)
sql = querys.sql1
df = pd.read_sql(sql, cnxn)
cnxn.close()

#qtd1 = df['mesanocompetencia'].value_counts()

#graph = pd.crosstab(index=df['mesanocompetencia'],columns=df['instrumento']).apply(lambda r: r/r.sum() *100,axis=1)
graph = pd.crosstab(df['mesanocompetencia'],df['instrumento'])
graph.plot(kind='bar', figsize=(200,60), grid=True, rot=0, legend=False)
plt.title('Quantidade de atendimetos por mês em 2017')
plt.xlabel('Quantidade de atendimentos')
plt.show()
