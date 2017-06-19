from servo import Servo
from state import State
from move import Move

import sys
import random


if len(sys.argv) == 2:
	movesNo = int(sys.argv[1])
	states = []
	for n in range (0,movesNo):
		state = State([])
		for i in range (1,7):
			if n != 0:
				servo = Servo(i,random.randint(-90,90))
			else:
				servo = Servo(i,0)
			state.addServo(servo)
		states.append(state)

Move(states).run(0.5)





