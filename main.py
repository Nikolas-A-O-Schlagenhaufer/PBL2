import pandas as pd
import matplotlib.pyplot as plt

def main():
	dados = pd.read_csv('data/samples.csv', sep=',', header=0)
	eixo = list(dados["'EEG Fp2'"].drop(0, axis=0).values)
	eixo = [float(valor) for valor in eixo]
	plt.plot(eixo)
	plt.show()

	
if __name__ == '__main__':
	main()ajuda