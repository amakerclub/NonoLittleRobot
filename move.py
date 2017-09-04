
from state import State
import json

class Move:
    _states=[]
    _distance=None
    """a Move is a sequence of states."""
    def __init__(self, iStates):
        """ Constructor
        :param State iStates: States composing this movement
        """
        self._states = iStates
        self._distance = None
        
    @property
    def states(self):
        return self._states
    
    @property
    def distance(self):
        return self._distance
    
    @distance.setter
    def distance(self, value):
        self._distance = value

    def toDict(self):
        statesString=[]
        for state in self._states:
            statesString.append(state.toDict(   ))
        return {'states': statesString , 'distance' : self._distance}

    def fromDict(self, dict):
        self._distance = dict('distance')
        self._states = []
        for state in dict('states'):
            self.states.append(State.fromDict(state))

