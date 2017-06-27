%matplotlib inline
import os
import sys
import pandas as pd
import pyodbc
import pandas.io.sql as psql
import matplotlib.pyplot as plt

cnxn = pyodbc.connect('DRIVER={Sql Server};SERVER=***;DATABASE=***;UID=***;PWD=***') 
cursor = cnxn.cursor()
sql = ("""select distinct(codrealizacao) as qtdrealizacoes, mesanocompetencia from historicorealizacoescliente""")

df = psql.read_sql(sql, cnxn)
cnxn.close()

#df[['mesanocompetencia','qtdrealizacoes']]

qtd = df['mesanocompetencia'].value_counts()
qtd.plot(kind='barh', figsize=(20,5), grid=True, rot=0, color='blue', legend=False)
plt.title('Quantidade de atendimetos por mês em 2017')
plt.xlabel('Quantidade de atendimentos')
plt.show()
