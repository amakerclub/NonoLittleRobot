from servo import Servo
from state import State

import sys

state0 = State([])

if len(sys.argv) == 2:
	for i in range (0,6):
		servo = Servo(i,int(sys.argv[1]))
		state0.addServo(servo)

	state0.move()





