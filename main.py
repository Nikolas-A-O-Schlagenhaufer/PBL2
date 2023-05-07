import pandas as pd
import matplotlib.pyplot as plt
from study import Study


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


def main():
	# tratar_arquivo_mental('S5-2.csv')

	# tratar_arquivo_motor('S5-1.csv')

	study = Study()
	# study.tests[1].list_subjects()
	# study.tests[1].subjects[0].data_sets[0].data.plot(subplots=True, grid=True)
	study.tests[1].get_subject(8).data_sets[0].data.plot(subplots=True, grid=True)
	plt.show()
	print(study.tests[1].get_subject_ids())


if __name__ == '__main__':
	main()