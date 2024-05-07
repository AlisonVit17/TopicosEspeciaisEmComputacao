import numpy as np
import pandas
import matplotlib.pyplot as plt
from scipy import stats

seid2021 = pandas.read_csv('Seid2021.csv')
seid2022 = pandas.read_csv('Seid2022.csv')
seid2023 = pandas.read_csv('Seid2023.csv')
dicionariParaMedias21 = {}
dicionariParaMedias22 = {}
dicionariParaMedias23 = {}
#print(seid2021.keys())

for i in range(len(seid2021['Funcao'])):
    if seid2021['Funcao'][i] not in dicionariParaMedias21.keys():
        dicionariParaMedias21[seid2021['Funcao'][i]] = []

    valor = seid2021['Pago'][i].split('$')
    dicionariParaMedias21[seid2021['Funcao'][i]].append(float(valor[1].replace(',', '')))


for i in range(len(seid2022['Funcao'])):
    if seid2022['Funcao'][i] not in dicionariParaMedias22.keys():
        dicionariParaMedias22[seid2022['Funcao'][i]] = []

    valor = seid2022['Pago'][i].split('$')
    dicionariParaMedias22[seid2022['Funcao'][i]].append(float(valor[1].replace(',', '')))


for i in range(len(seid2023['Funcao'])):
    if seid2023['Funcao'][i] not in dicionariParaMedias23.keys():
        dicionariParaMedias23[seid2023['Funcao'][i]] = []

    valor = seid2023['Pago'][i].split('$')
    dicionariParaMedias23[seid2023['Funcao'][i]].append(float(valor[1].replace(',', '')))

#Gráfico bloxplot de 2021
fig, ax = plt.subplots()

dicionariParaMedias21['ADMINISTRAÇÃO'].sort()
dicionariParaMedias21['DIREITOS DA CIDADANIA'].sort()
dicionariParaMedias21['SAÚDE'].sort()
dados = [dicionariParaMedias21['ADMINISTRAÇÃO'],
         dicionariParaMedias21['DIREITOS DA CIDADANIA'],
         dicionariParaMedias21['SAÚDE']]

plt.boxplot(dados)
xticks = ['Administração', 'Direitos da cidadania', 'Saúde']
ax.set_xticklabels(xticks)
ax.set_title('Função - Seid 2021')
ax.set_xlabel('Conjunto de Dados agrupados por função')
ax.set_ylabel('Valores')
plt.show()
print('Seid 2021: ', dicionariParaMedias21.keys())
#for i in dicionariParaMedias21.keys():
#    print(dicionariParaMedias21[i])
print('Seid 2021 (Administração): \n   Média = ',
      np.mean(dicionariParaMedias21['ADMINISTRAÇÃO']), '\n   Mediana = ',
      np.median(dicionariParaMedias21['ADMINISTRAÇÃO']),
      '\n   Moda = ', stats.mode(dicionariParaMedias21['ADMINISTRAÇÃO']),
        '\n   Desvio padrão = ', np.std(dicionariParaMedias21['ADMINISTRAÇÃO']))
print('Seid 2021 (Direitos a cidadania): \n   Média = ',
      np.mean(dicionariParaMedias21['DIREITOS DA CIDADANIA']),
      '\n   Mediana = ', np.median(dicionariParaMedias21['DIREITOS DA CIDADANIA']),
      '\n   Moda = ', stats.mode(dicionariParaMedias21['DIREITOS DA CIDADANIA']),
        '\n   Desvio padrão = ', np.std(dicionariParaMedias21['DIREITOS DA CIDADANIA']))
print('Seid 2021 (Direitos a cidadania): \n   Média = ',
      np.mean(dicionariParaMedias21['SAÚDE']), '\n   Mediana = ',
      np.median(dicionariParaMedias21['SAÚDE']),
      '\n   Moda = ', stats.mode(dicionariParaMedias21['SAÚDE']),
        '\n   Desvio padrão = ', np.std(dicionariParaMedias21['SAÚDE']))

print('')
#Gráfico bloxplot de 2022
fig, ax = plt.subplots()
dicionariParaMedias22['ADMINISTRAÇÃO'].sort()
dicionariParaMedias22['DIREITOS DA CIDADANIA'].sort()
dicionariParaMedias22['SAÚDE'].sort()

dados = [dicionariParaMedias22['ADMINISTRAÇÃO'],
         dicionariParaMedias22['DIREITOS DA CIDADANIA'],
         dicionariParaMedias22['SAÚDE']]
plt.boxplot(dados)
xticks = ['Administração', 'Direitos da cidadania', 'Saúde']
ax.set_xticklabels(xticks)
ax.set_title('Função - Seid 2022')
ax.set_xlabel('Conjunto de Dados agrupados por função')
ax.set_ylabel('Valores')
plt.show()
print('Seid 2022 (Administração): \n   Média = ',
      np.mean(dicionariParaMedias22['ADMINISTRAÇÃO']),
      '\n   Mediana = ', np.median(dicionariParaMedias22['ADMINISTRAÇÃO']),
      '\n   Moda = ', stats.mode(dicionariParaMedias22['ADMINISTRAÇÃO']),
        '\n   Desvio padrão = ', np.std(dicionariParaMedias22['ADMINISTRAÇÃO']))
print('Seid 2022 (Direitos a cidadania): \n   Média = ',
      np.mean(dicionariParaMedias22['DIREITOS DA CIDADANIA']),
      '\n   Mediana = ', np.median(dicionariParaMedias22['DIREITOS DA CIDADANIA']),
      '\n   Moda = ', stats.mode(dicionariParaMedias22['DIREITOS DA CIDADANIA']),
        '\n   Desvio padrão = ', np.std(dicionariParaMedias22['DIREITOS DA CIDADANIA']))
print('Seid 2022 (Direitos a cidadania): \n   Média = ',
      np.mean(dicionariParaMedias22['SAÚDE']),
      '\n   Mediana = ', np.median(dicionariParaMedias22['SAÚDE']),
      '\n   Moda = ', stats.mode(dicionariParaMedias22['SAÚDE']),
        '\n   Desvio padrão = ', np.std(dicionariParaMedias22['SAÚDE']))

#for i in dicionariParaMedias22.keys():
#    print(dicionariParaMedias22[i])


print('')
#Gráfico bloxplot de 2023
fig, ax = plt.subplots()
dicionariParaMedias23['ADMINISTRAÇÃO'].sort()
dicionariParaMedias23['DIREITOS DA CIDADANIA'].sort()
dicionariParaMedias23['SAÚDE'].sort()

dados = [dicionariParaMedias23['ADMINISTRAÇÃO'],
         dicionariParaMedias23['DIREITOS DA CIDADANIA'],
         dicionariParaMedias23['SAÚDE']]
plt.boxplot(dados)
xticks = ['Administração', 'Direitos da cidadania', 'Saúde']
ax.set_xticklabels(xticks)
ax.set_title('Função - Seid 2023')
ax.set_xlabel('Conjunto de Dados agrupados por função')
ax.set_ylabel('Valores')
plt.show()

print('Seid 2023: ', dicionariParaMedias23.keys())
print('Seid 2023 (Administração): \n   Média = ',
      np.mean(dicionariParaMedias23['ADMINISTRAÇÃO']),
      '\n   Mediana = ', np.median(dicionariParaMedias23['ADMINISTRAÇÃO']),
      '\n   Moda = ', stats.mode(dicionariParaMedias23['ADMINISTRAÇÃO']),
        '\n   Desvio padrão = ', np.std(dicionariParaMedias23['ADMINISTRAÇÃO']))
print('Seid 2023 (Direitos a cidadania): \n   Média = ',
      np.mean(dicionariParaMedias23['DIREITOS DA CIDADANIA']),
      '\n   Mediana = ', np.median(dicionariParaMedias23['DIREITOS DA CIDADANIA']),
      '\n   Moda = ', stats.mode(dicionariParaMedias23['DIREITOS DA CIDADANIA']),
        '\n   Desvio padrão = ', np.std(dicionariParaMedias23['DIREITOS DA CIDADANIA']))
print('Seid 2023 (Direitos a cidadania): \n   Média = ',
      np.mean(dicionariParaMedias23['SAÚDE']),
      '\n   Mediana = ', np.median(dicionariParaMedias23['SAÚDE']),
      '\n   Moda = ', stats.mode(dicionariParaMedias23['SAÚDE']),
        '\n   Desvio padrão = ', np.std(dicionariParaMedias23['SAÚDE']))

#for i in dicionariParaMedias23.keys():
#    print(dicionariParaMedias23[i])
