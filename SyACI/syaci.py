import numpy as np
import pandas as pd
from nltk import word_tokenize as tokenize
from urllib import request as req


class syaci(object):
	"""docstring for syaci"""
	def __init__(self, arg):
		super(syaci, self).__init__()
		self.arg = arg
		setRules(self);
		
	def setRules(self):
		url = "http://www.gutenberg.org/files/2554/2554.txt"
		response = request.urlopen(url)
		raw = response.read().decode('utf8')
		type(raw)
		raw[:75]