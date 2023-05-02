from test import Test
import os
import pickle

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
	
if __name__ == '__main__':
	study = Study()
	print(study)