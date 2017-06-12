import time

from state import State

class Move:
	def __init__(self,iStates):
		self._states = iStates
		self._distance = None

	def run(self):
		for state in self._states:
			state.move()
			time.sleep(2)

		self._states[0].move()
