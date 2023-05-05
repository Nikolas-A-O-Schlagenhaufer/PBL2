from test import Test
import os
import pickle
import pandas as pd

class Study:
	"""
	Represents a study, with all its tests.

	Attributes:
	-----------
	- tests: list of Test objects

	Methods:
	--------
	- add_tests: adds all tests in the directory selected for the study
	- list_tests: lists all tests in the study, with their subjects
	"""
	def __init__(self, directory:str='treated_data'):
		self.tratar_arquivos()
		self.tests = self.add_tests(directory)
		
	def add_tests(self, directory:str) -> list:
		"""
		Adds all tests in the directory selected for the study.
		"""
		subfolders = [f.name for f in os.scandir(directory) if f.is_dir()]
		tests = [Test(directory, subfolder) for subfolder in subfolders]
		return tests
	
	def __str__(self) -> str:
		"""
		Returns a string representation of the study.
		"""
		result = f"{'STUDY':-^30}\n"
		result += f"Study with {len(self.tests)} test(s):\n"
		for test in self.tests:
			result += f"{test.__str__()}\n"
		result += f"{'STUDY':-^30}"
		return result
	
	def list_tests(self) -> None:
		"""
		Lists all tests in the study, with their subjects.
		"""
		for test in self.tests:
			print(test)

	def save(self, filename:str='study.pkl') -> None:
		"""
		Saves the study in a pickle file.
		"""
		with open(filename, 'wb') as file:
			pickle.dump(self, file)
			print(f"Study saved in {filename}")

	@classmethod
	def load(cls, filename:str='study.pkl') -> object:
		"""
		Loads the study from a pickle file.
		"""
		with open(filename, 'rb') as file:
			study = pickle.load(file)
			print(f"Study loaded from {filename}")
			return study
		
	def tratar_arquivos(self):
		"""
		Realiza o tratamento dos dados antes de iniciar o estudo.
		"""
		raw_files = os.listdir('data/motor_movement')
		treated_files = os.listdir('treated_data/motor_movement')
		right_files = [file for file in raw_files if file[:4] not in [file[:4] for file in treated_files]]
		for file in right_files:
			caminho = f"data/motor_movement/{file}"
			columns = ['Time and date','Fc5','Fc3','Fc1','Fcz','Fc2','Fc4','Fc6','C5',
				'C3','C1','Cz','C2','C4','C6','Cp5','Cp3','Cp1','Cpz','Cp2','Cp4','Cp6',
				'Fp1','Fpz','Fp2','Af7','Af3','Afz','Af4','Af8','F7','F5','F3','F1',
				'Fz','F2','F4','F6','F8','Ft7','Ft8','T7','T8','T9','T10','Tp7','Tp8',
				'P7','P5','P3','P1','Pz','P2','P4','P6','P8','Po7','Po3','Poz','Po4',
				'Po8','O1','Oz','O2','Iz','EDF Annotations']
			dados = pd.read_csv(caminho, header=None, names=columns, skiprows=2)
			for idx in range(len(dados)):
				dados['Time and date'].iat[idx] = dados['Time and date'].iat[idx][2:-2]
			dados.to_csv(f"treated_data/motor_movement/{file[:-4]}-tratado.csv", index=False)
	
if __name__ == '__main__':
	study = Study()
	print(study)