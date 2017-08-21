from servo import Servo
from state import State
from move import Move

import sys
import random
import pickle


class Darwin:
    """Darwin
     - creates a world of 30 random Move
     Loop on
     - get a subset of 4
       - evaluate each one (if not already done)
       - removes two worst performers
       - keeps two best performers
       - creates 2 children with 2 best performers"""


    def __init__(self):
        self.world = []
    pass

    def randomMove(self, statesCount):
        states = []
        for n in range (0,statesCount):
            state = State([])
            for i in range (1,7):
                if n != 0:
                    servo = Servo(i,random.randint(-90,90))
                else:
                    servo = Servo(i,0)
                state.addServo(servo)
            states.append(state)
        return Move(states)


    def createWorld(self, populationCount,statesCount, outputFile):
        print ('createWorld: start')
        for i in range (0,populationCount):
            self.world.append(self.randomMove(statesCount))
        print(self.world.toDict())
        pickle.dump(self.world,outputFile)
        print ('createWorld: end')



if __name__ == '__main__':
    print ('Main : start')
    d =Darwin()
    d.createWorld ( int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
    print ('Main : end')