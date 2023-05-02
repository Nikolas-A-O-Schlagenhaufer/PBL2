from data_set import DataSet
import os

class Subject:
	"""
	Rerpresents a subject, with its id and its data.

	Attributes:
	-----------
	- id: id of the subject
	- data: list of dataframes, each dataframe corresponding to a set of data
	for the same subject

	Methods:
	--------
	- get_data: returns a list of dataframes, each dataframe corresponding to a
	set of data for the same subject
	"""
	def __init__(self, directory:str, subfolder:str, subject:str):
		self.id = int(subject[1:])
		self.data_sets = self.add_data_sets(directory, subfolder, subject)

	def __str__(self) -> str:
		"""
		Returns a string representation of the subject.
		"""
		return f"Subject {self.id} with {len(self.data_sets)} data set(s)"

	def add_data_sets(self, directory:str, subfolder:str, subject:str) -> list:
		"""
		"""
		files = os.listdir(f"{directory}/{subfolder}")
		data_sets = [DataSet(directory, subfolder, file) for file in files if file.startswith(f"{subject}-")]
		return data_sets