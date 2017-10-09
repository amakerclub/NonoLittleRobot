from servo import Servo
from state import State
from move import Move
from evolution import Evolution
from executor import Executor

from StringIO import StringIO
import sys
import random
import json
import pprint
import random


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
        self.executor = Executor(0.4)
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
            self.world[ str(i)]= self.randomMove(statesCount)#.toDict()
        pprint.pprint(self.world)

        print ('createWorld: end')

    def saveWorld(self,outputfile):
        with open ( outputfile, 'w+') as f:
            json.dump(d.world,f)

    def loadWorld(self,inputfile):
        with open (inputfile) as f:
            self.world=json.load(f)

    def darwinLoop(self, maxLoops, parentCount=4, parentKept=2):
        ### Loop on world, evaluate n parents, keep only m best ones and replace others by evolution from kept best ones
        j = 0
        print "darwin loop started"
        while (j < maxLoops):
            print "--- Darwin in the while loop "+str(j)
            ### Store best Move and distance
            bestDistance = 0
            bestMove = 0


            evalMovesIndexes = random.sample(range (0, len(self.world)), parentCount)
            print "evalMoves="
            print evalMovesIndexes
            print "darwin after evalmoves"

            for i in evalMovesIndexes:
                print "darwin in the for loop"
                print self.world
                print self.world[str(i)]
                if ( self.world[str(i)]._distance is None ):
                    self.world[str(i)]._distance= self.executor.run(self.world[str(i)])
                print "Executor done"
            # sort evalMoves
            print "evalMovesSorted="
            evalMovesSorted=sorted(evalMovesIndexes, key=lambda i:self.world[str(i)]._distance)
            print evalMovesSorted

            #keep 2 bests (2 last)
            # We dont need to do anything to keep them...

            # replace 2 worsts by children of 2 best ==> Verify the content of simpleCrossover execution
            e = Evolution()
            print ("CrossingOver : last and last-1")
            pprint.pprint(str(self.world[str(evalMovesSorted[-1])]))
            pprint.pprint(str(self.world[str(evalMovesSorted[-2])]))
            print ("CrossOver result : ")
            (A,B) = e.simpleCrossover(self.world[str(evalMovesSorted[-1])], self.world[str(evalMovesSorted[-2])])

            # Uncomment to use mutation (NOT TESTED YET)
            # A = mutation(0.05, 10, A)
            # B = mutation(0.05, 10, B)

            self.world[str(evalMovesSorted[0])] = A
            self.world[str(evalMovesSorted[1])] = B

            pprint.pprint(str(self.world[str(evalMovesSorted[0])]))
            pprint.pprint (str(self.world[str(evalMovesSorted[1])]))

            j+=1


if __name__ == '__main__':
    print ('Main : start')
    d =Darwin()
    print ('Arguments : loopCount populationCount statesPerMoveCount fileName')
    #with open('./test','w+') as f:
    #    json.dump(d.randomMove(3).toDict(),f)
    d.createWorld ( int(sys.argv[2]), int(sys.argv[3]))
    d.darwinLoop(1)
    #d.saveWorld(sys.argv[4])
    #d.loadWorld(sys.argv[4])

    pprint.pprint(d.world)

    print ('Main : end')
