import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import lfilter

def tratar_arquivo_mental(arquivo:str):
	caminho = f"data/mental/{arquivo}"
	columns = ['Time and date','Fp1','Fp2','F3','F4','F7','F8','T3','T4','C3',
	    'C4','T5','T6','P3','P4','O1','O2','Fz','Cz','Pz','A2-A1','ECG ECG',
		'EDF Annotations',]
	dados = pd.read_csv(caminho, header=None, names=columns, skiprows=2)
	# print(dados.head(20))
	for idx in range(len(dados)):
		dados['Time and date'].iat[idx] = dados['Time and date'].iat[idx][2:-2]
	# print(dados.head(20))
	dados.to_csv(f"treated_data/mental/{arquivo[:-4]}-tratado.csv", index=False)

def tratar_arquivo_motor(arquivo:str):
	caminho = f"data/motor_movement/{arquivo}"
	columns = ['Time and date','Fc5','Fc3','Fc1','Fcz','Fc2','Fc4','Fc6','C5',
	    'C3','C1','Cz','C2','C4','C6','Cp5','Cp3','Cp1','Cpz','Cp2','Cp4','Cp6',
		'Fp1','Fpz','Fp2','Af7','Af3','Afz','Af4','Af8','F7','F5','F3','F1',
		'Fz','F2','F4','F6','F8','Ft7','Ft8','T7','T8','T9','T10','Tp7','Tp8',
		'P7','P5','P3','P1','Pz','P2','P4','P6','P8','Po7','Po3','Poz','Po4',
		'Po8','O1','Oz','O2','Iz','EDF Annotations']
	dados = pd.read_csv(caminho, header=None, names=columns, skiprows=2)
	for idx in range(len(dados)):
		dados['Time and date'].iat[idx] = dados['Time and date'].iat[idx][2:-2]
	dados.to_csv(f"treated_data/motor_movement/{arquivo[:-4]}-tratado.csv", index=False)


def ler_tratado_mental(arquivo:str) -> pd.DataFrame:
	caminho = f"treated_data/mental/{arquivo}"
	dados = pd.read_csv(caminho, parse_dates=['Time and date'])
	return dados


def ler_tratado_motor(arquivo:str) -> pd.DataFrame:
	caminho = f"treated_data/motor_movement/{arquivo}"
	dados = pd.read_csv(caminho, parse_dates=['Time and date'])
	return dados


def plot_all_columns(data:pd.DataFrame):
	# plot all columns
	plt.figure(figsize=(20, 10))
	for i in range(len(data.columns)):
		plt.subplot(len(data.columns), 1, i+1)
		name = data.columns[i]
		plt.plot(data[name])
		plt.title(name, y=0, loc='right')
	plt.show()


def main():
	# tratar_arquivo_mental('subject5-2.csv')
	# data = ler_tratado_mental('subject0-2-tratado.csv')

	# plot_all_columns(data)

	# tratar_arquivo_motor('S1-1.csv')
	data = ler_tratado_motor('S1-1-tratado.csv')

	dados_calculados = pd.DataFrame()
	dados_calculados['Time and date'] = data['Time and date']
	dados_calculados['Fp1 - F3'] = data['Fp1'] - data['F3']
	dados_calculados['F3 - C3'] = data['F3'] - data['C3']
	dados_calculados['Fz - Cz'] = data['Fz'] - data['Cz']
	dados_calculados['Cz - Pz'] = data['Cz'] - data['Pz']
	dados_calculados['Fp2 - F4'] = data['Fp2'] - data['F4']
	dados_calculados['F4 - C4'] = data['F4'] - data['C4']

	dados_calculados.drop('Time and date', inplace=True, axis=1)

	for column in dados_calculados.columns:
		signal = dados_calculados[column]
		n = 50
		b = [1.0 / n] * n
		a = 1
		dados_calculados[column] = lfilter(b, a, signal)

	plot_all_columns(dados_calculados)


if __name__ == '__main__':
	main()