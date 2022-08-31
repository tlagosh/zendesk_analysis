import pandas as pd

df = pd.read_csv('tickets.csv')


print('######################\n')
print('Filas Duplicadas: ' + str(df.duplicated().any()) + '\n')
print('######################\n')

print(df.info())
