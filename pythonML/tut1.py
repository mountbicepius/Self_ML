from sklearn import datasets
from sklearn import svm
import pickle


class tut1(object):
	"""docstring for ClassName"""
	def __init__(self):
		super(tut1, self).__init__()
		
	def mainFunc():
		iris = datasets.load_iris()
		digits = datasets.load_digits()
		print(digits.data)
		clf = svm.SVC(gamma=0.001, C=100.)
		print(clf.fit(digits.data[:-1], digits.target[:-1]))
		print(clf.predict(digits.data[-1:]))
		
	
tut1.mainFunc()
		