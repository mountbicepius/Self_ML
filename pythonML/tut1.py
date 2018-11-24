from sklearn import datasets

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		dataset(self)

	def dataset(self):
		iris = datasets.load_iris()
		digits = datasets.load_digits()
		print(digits.data)