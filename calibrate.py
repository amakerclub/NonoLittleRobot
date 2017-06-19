from servo import Servo
from state import State
from move import Move

import sys
import time

if len(sys.argv) == 4:
	servo_num = int(sys.argv[1])
	servo_min = int(sys.argv[2]) #150  # Min pulse length out of 4096
	servo_max = int(sys.argv[3]) #600  # Max pulse length out of 4096

	if servo_min > servo_max:
		sys.exit(1)
	
	start = 100
	value = servo_min

	while value <= servo_max:
		# Move servo on channel O between extremes.
		#for i in range(0, 1):
		servo = Servo(servo_num,value)
		servo.move()
		time.sleep(1)
		print ("Value: %d" % value)
		value += 10 #servo_max - servo_min # 50
		#print ('Continue? Y/N')
		#inValue = raw_input()
		#if inValue != 'Y':
		#	break
	
	servo_zero = int((servo_max + servo_min) / 2.0)
	#servo = Servo(servo_num,300)
	#servo.move()

	for i in range (1,7):
		servo = Servo(i,servo_zero)
		servo.move()
