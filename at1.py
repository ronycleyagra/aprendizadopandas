'''
Disciplina: Processos estocásticos
Aluno: Ronycley Gonçalves Agra
Matrícula: 20141121044
Data: 07/06/2016
Atividade 1
'''
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

dataset = open ('dados.csv', 'r')

quantidades = []
datas = []

print('1 = Brasil\n2 = Ceará\n3 = Distrito Federal\n4 = Minas Gerais\n5 = Parana\n6 = Rio de Janeiro\n7 = Rio Grande do Sul\n8 = Santa Catarina\n9 = São Paulo\n')
a = eval(input('Digite o Numero da Cidade: '))

for line in dataset: 
    line2 = line.strip()
    words = {i:word for i, word in enumerate(line2.split(','))}
    if ( words[a] == '' or words[a] == ' '): 
        quantidades.append(None)
    else: 
        quantidades.append(words[a])
    datas.append(mdates.datestr2num(words[0]))
dataset.close()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xticks(datas) # Tickmark + label at every plotted point
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
fig.autofmt_xdate(rotation=90)
fig.tight_layout()

plt.plot(datas, quantidades)

plt.title('Buscas por "Gripe"')
plt.xlabel('Cidade')
plt.ylabel('Quantidades')

# Format the x-axis for dates (label formatting, rotation)


plt.show()
