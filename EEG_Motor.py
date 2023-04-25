import pandas as pd
import matplotlib.pyplot as plt

def main():
	dados = pd.read_csv('data/EEG_Motor01.csv', sep=',', header=0)
	eixo = list(dados["'Fc5.'"].drop(0, axis=0).values)
	eixo = [float(valor) for valor in eixo]
	plt.plot(eixo)
	plt.show()
	
if __name__ == '__main__':
	main()