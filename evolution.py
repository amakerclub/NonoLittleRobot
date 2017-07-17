import random
from state import State
from move import Move

class Evolution:

    """Evolution handles meyose and mutation of moves"""

    def __init__(self):
        pass

    def meyoseByState(self,moveA, moveB):
        """Meyose by exchange of entire state between two patents"""
        states = State([])
        movelenght = len(moveA.states)
        for stateNumber in range(0,movelenght):
            if random.randrange(0,1) > 0.5 :
                states[stateNumber]= moveA.states[stateNumber]
            else:
                states[stateNumber]= moveB.states[stateNumber]
        return Move(states)

    def meyoseByServo(self,moveA, moveB):
        """Meyose by exchange of servos in states between two patents"""

        states = State([])
        movelenght = len(moveA.states)
        for stateNumber in range(0,movelenght):
            statelenght=len(moveA.states[stateNumber].servos)
            states[stateNumber] = []
            for servoNumber in range (0, statelenght):
                if random.randrange(0,1) > 0.5 :
                    states[stateNumber].addServo( moveA.states[stateNumber].servos[servoNumber])
                else:
                    states[stateNumber].addServo(moveB.states[stateNumber].servos[servoNumber])

        return Move(states)

    def mutation(self, movement, probability, maxAbsoluteChange):
        """mutation adds a bit of randomness in the chain by changing few servo positions of a movement"""
        for state in movement.states:
            for servo in state._servos:
                if probability>random.randrange(0,1):
                    servo._position=maxAbsoluteChange*(1-random.randrange(0,2))
        return movement

