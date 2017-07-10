import time

from state import State


class Move:
    def __init__(self, iStates):
        self._states = iStates
        self._distance = None

    def toDict(self):
        return {'states': self._states , 'distance' : self._distance}

    def fromDict(self, dict):
        self._distance  = dict('distance')
        self.states=[]
        for state in dict('states'):
            self.states.append(State.fromDict(state))


    def run(self, iSleepTime):
        for state in self._states:
            state.move()
            time.sleep(iSleepTime)

        self._states[0].move()


