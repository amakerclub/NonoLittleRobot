from move import Move
from StringIO import StringIO

import sys
import time
import json


class io:
	def __init__(self):
        	

	def save(self, move, target):
		with open (target, 'a+') as fileout:
			json.dump(move, target)

	def load(self, source):
		j = json.loads(source);


