from subject import Subject
import os

class Test:
	"""
	Rerpresents a test, with its name and its subjects.

	Attributes:
	-----------
	- name: name of the test
	- subjects: list of Subject objects

	Methods:
	--------
	- add_subjects: adds all subjects in the directory selected for the test
	- list_subjects: lists all subjects in the test
	"""
	def __init__(self, directory:str, subfolder:str):
		self.name = subfolder
		self.subjects = self.add_subjects(directory, subfolder)

	def __str__(self) -> str:
		"""
		Returns a string representation of the test.
		"""
		return f"Test {self.name} with {len(self.subjects)} subject(s)"

	def add_subjects(self, directory:str, subfolder:str) -> list:
		"""
		Adds all subjects in the directory selected for the test.
		"""
		files = os.listdir(f"{directory}/{subfolder}")
		subjects = list(set([int(file.split('-')[0][1:]) for file in files]))
		subjects.sort()
		subjects = [Subject(directory, subfolder, f"S{subject}") for subject in subjects]
		return subjects
	
	def list_subjects(self) -> None:
		"""
		Lists all subjects in the test.
		"""
		for subject in self.subjects:
			print(subject)

if __name__ == '__main__':
	directory = 'treated_data'
	subfolder = 'motor_movement'
	files = os.listdir(f"{directory}/{subfolder}")
	subjects = list(set([int(file.split('-')[0][1:]) for file in files]))
	subjects.sort()
	print(subjects)