import pandas as pd
import matplotlib.pyplot as plt

def main():
	dados = pd.read_csv('data/Subject_001.csv', sep=',', header=0).drop(0, axis=0)
	# print(dados.head())
	dados.columns = [item[1:-1] for item in dados.columns]
	dados.drop('EDF Annotations', axis=1, inplace=True)
	# print(dados.head())
	for column in list(dados.columns)[1:10]:
		dados[column] = dados[column].astype(float)
	# erros = []
	# for i in range(len(dados)):
		# try:
			# float(dados['EEG C3'].iloc[i])
		# except:
			# erros.append(i)
	# print(erros)
	# print(dados['EEG C3'].iloc[erros[0]])

if __name__ == '__main__':
	main()