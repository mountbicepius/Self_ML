#Systemic Augumented Cognitive Intelligence(SyACI)
"""
Author : Anirudh Srivastav 
Date: 12.08.2016 14:36:44

Description: An NLP based , generative hyperinteractive model, 
requires minimal Data to train but requries multi user environment to
optiimise itself on virtual or real enviroments.

Tags: seq2seq, NLTK , Keras

"""


import numpy as np
import pandas as pd
from nltk import word_tokenize as tokenize
from nltk.book import *
from urllib import request as req


class syaci(object):
	"""docstring for syaci"""
	def __init__(self, arg):
		super(syaci, self).__init__()
		self.arg = arg
    
	def setRules(self):
		url = "https://www.gutenberg.org/cache/epub/66588/pg66588-images.html"
		response = req.urlopen(url)
		raw = response.read().decode('utf8')
		type(raw)
		raw[:75]
  
  def execute(text):
    print(len(set(text)) / len(text))

  def setLength(count,total):
    return count * total /100
  
  def pass_text(self, arg):
		sdata = pd.read_csv()
		for x in sdata(1,1000):
      print("ok")