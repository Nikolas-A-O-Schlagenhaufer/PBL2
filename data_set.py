import pandas as pd
from scipy.signal import lfilter
import matplotlib.pyplot as plt

class DataSet:
	"""
	Represents one of many datasets from a subject. Each dataset has a unique
	id and a dataframe with the data. The dataframe has the following columns:
	- Fp1 - F3
	- F3 - C3
	- Fz - Cz
	- Cz - Pz
	- Fp2 - F4
	- F4 - C4

	Atributes:
	----------
	- id: unique id of the dataset
	- data: dataframe with the data of the dataset

	Methods:
	--------
	- filter: returns the data filtered with a low-pass filter
	- add_data: returns a dataframe with the data of the dataset
	"""
	def __init__(self, directory:str, subfolder:str, file:str) -> None:
		self.id = int(file.split('-')[1])
		self.data = self.add_data(directory, subfolder, file, derivatives=True, filter=True)

	def __str__(self) -> str:
		"""
		Returns a string representation of the dataset.
		"""
		return f"Dataset {self.id} with {len(self.data)} samples"
	
	def filter(self, data:pd.DataFrame) -> pd.DataFrame:
		"""
		Returns the data filtered with a low-pass filter.
		"""
		for column in data.columns:
			signal = data[column]
			n = 50
			b = [1.0 / n] * n
			a = 1
			data[column] = lfilter(b, a, signal)
		return data
	
	def add_derivatives(self, data:pd.DateOffset) -> pd.DataFrame:
		"""
		Returns the data with new columns, each column corresponding to the
		derivative of the original columns.
		"""
		de = pd.DataFrame()
		for column in data.columns:
			de[f"d_{column}"] = data[column].diff()
		data = pd.concat([data, de], axis=1)
		data = self.filter(data)
		data = data.dropna()
		return data
	
	def add_data(self, directory:str, subfolder:str, file:str, **kwargs) -> pd.DataFrame:
		"""
		Returns a dataframe with the data of the dataset. The dataframe has the
		following columns:
		- Fp1 - F3
		- F3 - C3
		- Fz - Cz
		- Cz - Pz
		- Fp2 - F4
		- F4 - C4

		Parameters:
		-----------
		- directory: directory where the data is stored
		- subfolder: subfolder where the data is stored
		- file: file where the data is stored
		- filter: boolean indicating if the data should be filtered or not
		"""
		treated = pd.read_csv(f"{directory}/{subfolder}/{file}")
		calc = pd.DataFrame()
		calc['Fp1 - F3'] = treated['Fp1'] - treated['F3']
		calc['F3 - C3'] = treated['F3'] - treated['C3']
		calc['Fp1 - F7'] = treated['Fp1'] - treated['F7']
		try:
			calc['F7 - T7'] = treated['F7'] - treated['T7']
		except KeyError:
			calc['F7 - T3'] = treated['F7'] - treated['T3']
		calc['Fz - Cz'] = treated['Fz'] - treated['Cz']
		calc['Cz - Pz'] = treated['Cz'] - treated['Pz']
		calc['Fp2 - F4'] = treated['Fp2'] - treated['F4']
		calc['F4 - C4'] = treated['F4'] - treated['C4']
		calc['Fp2 - F8'] = treated['Fp2'] - treated['F8']
		try:
			calc['F8 - T8'] = treated['F8'] - treated['T8']
		except KeyError:
			calc['F8 - T4'] = treated['F8'] - treated['T4']
		if 'filter' not in kwargs or kwargs['filter']:
			calc = self.filter(calc)
		if 'derivatives' in kwargs and kwargs['derivatives']:
			calc = self.add_derivatives(calc)
		calc = calc[(calc.T != 0).any()]
		return calc
	
if __name__ == "__main__":
	dataset = DataSet('treated_data', 'motor_movement', 'S1-1-tratado.csv')
	print(dataset)
	dataset.data.plot(subplots=True, grid=True)
	plt.show()