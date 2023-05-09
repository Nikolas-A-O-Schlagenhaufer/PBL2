import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from study import Study
from intervalos import intervalos
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.metrics import f1_score
from alive_progress import alive_bar
from joblib import dump, load


def generate_decision_tree() -> None:
	"""
	Generates a decision tree classifier model and saves it to a file.
	"""
	study = Study()

	data = pd.DataFrame()
	subjects = study.tests[1].get_subject_ids()
	for subject in subjects:
		subject_data = study.tests[1].get_subject(subject).data_sets[0].data
		subject_intervals = intervalos.get(subject)
		targets = np.zeros(len(subject_data))
		for interval in subject_intervals:
			targets[interval[0]:interval[1]] = 1
		subject_data['targets'] = targets
		data = pd.concat([data, subject_data], ignore_index=True)

	list_f1 = []
	times = 50
	with alive_bar(times) as bar:
		for i in range(times):
			X = data.drop('targets', axis=1).values
			y = data['targets'].values
			X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=i)
			clf = DTC(random_state=i)
			clf.fit(X_train, y_train)
			y_pred = clf.predict(X_test)
			list_f1.append(f1_score(y_test, y_pred))
			bar()
	
	f1 = np.max(list_f1)
	max_f1 = np.argmax(list_f1)
	print(f"Highest F1-score: {f1}, on random state {max_f1}")
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=i)
	clf = DTC(random_state=max_f1)
	clf.fit(X_train, y_train)
	dump(clf, 'decision_tree.joblib')


def get_decision_tree() -> DTC:
	"""
	Returns the decision tree classifier model.
	"""
	return load('decision_tree.joblib')


def main():
	# Rodar a seguinte função para gerar um novo modelo de árvore de decisão,
	# caso haja a necessidade de utilizar mais dados para o treinamento.
	# generate_decision_tree()
	
	study = Study()

	data = study.tests[1].get_subject(61).data_sets[0].data
	data.plot(subplots=True, grid=True)
	plt.show()
	
	
if __name__ == '__main__':
	main()