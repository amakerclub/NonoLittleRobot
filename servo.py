from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


pwm = Adafruit_PCA9685.PCA9685()
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)


class Servo:
	
	def __init__(self,iId,iPosition):
		self._id = iId
		self._position = iPosition

	def move(self):
		print("Moving %d to position %d" % (self._id,self._position))
		pwm.set_pwm(self._id, 0, self._position)

	def print2(self):
		print("Servo: _id: %d, _position: %d" % (self._id,self._position))
