import time

from state import State

class Move:
	def __init__(self,iStates):
		self._states = iStates
		self._distance = None

	def run(self,iSleepTime):
		for state in self._states:
			state.move()
			time.sleep(iSleepTime)

		self._states[0].move()
