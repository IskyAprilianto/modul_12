import pandas as pd

data = pd.read_csv("Negara.csv")

df = pd.DataFrame(data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print('Data frame: ')
print(df)

print('Data mean: ')
print(mean)

print('Data Standard Deviation: ')
print(std)

mean.to_csv('NegaraMean.csv')
std.to_csv('NegaraStandarDeviasi.csv')
print('File Berhasil Dibuat')