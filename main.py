import pandas as pd
import matplotlib.pyplot as plt

def tratar_arquivo(arquivo:str):
	caminho = f"data/{arquivo}"
	columns = ['Time and date','EEG Fp1','EEG Fp2','EEG F3','EEG F4','EEG F7',
	    'EEG F8','EEG T3','EEG T4','EEG C3','EEG C4','EEG T5','EEG T6','EEG P3',
		'EEG P4','EEG O1','EEG O2','EEG Fz','EEG Cz','EEG Pz','EEG A2-A1',
		'ECG ECG','EDF Annotations',]
	dados = pd.read_csv(caminho, header=None, names=columns, skiprows=2)
	# print(dados.head(20))
	for idx in range(len(dados)):
		dados['Time and date'].iat[idx] = dados['Time and date'].iat[idx][2:-2]
	# print(dados.head(20))
	dados.to_csv(f"treated_data/{arquivo[:-4]}-tratado.csv", index=False)


def ler_parquet(arquivo:str) -> pd.DataFrame:
	caminho = f"treated_data/{arquivo}"
	dados = pd.read_csv(caminho, parse_dates=['Time and date'])
	print(dados.head(20))
	print(dados.dtypes)
	return dados


def plot_all_columns(data:pd.DataFrame):
	# plot all columns
	plt.figure(figsize=(20, 10))
	for i in range(1,len(data.columns)):
		plt.subplot(len(data.columns), 1, i+1)
		name = data.columns[i]
		plt.plot(data[name])
		plt.title(name, y=0, loc='right')
	plt.show()


def main():
	# tratar_arquivo('subject5-2.csv')
	data = ler_parquet('subject5-2-tratado.csv')

	plot_all_columns(data)

if __name__ == '__main__':
	main()