from servo import Servo
from state import State
from move import Move

from StringIO import StringIO
import sys
import random
import json
import pprint
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
        self.world = {}
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


    def createWorld(self, populationCount,statesCount):
        print ('createWorld: start')
        for i in range (0,populationCount):
            self.world[ str(i)]= self.randomMove(statesCount).toDict()
        pprint.pprint(self.world)

        print ('createWorld: end')

    def saveWorld(self,outputfile):
        with open ( outputfile, 'w+') as f:
            json.dump(d.world,f)

    def loadWorld(self,inputfile):
        with open (inputfile) as f:
            self.world=json.load(f)

if __name__ == '__main__':
    print ('Main : start')
    d =Darwin()

    #with open('./test','w+') as f:
    #    json.dump(d.randomMove(3).toDict(),f)
    d.createWorld ( int(sys.argv[1]), int(sys.argv[2]))
    d.saveWorld(sys.argv[3])
    d.loadWorld(sys.argv[3])
    pprint.pprint(d.world)

    print ('Main : end')