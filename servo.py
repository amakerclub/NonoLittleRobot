from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


pwm = Adafruit_PCA9685.PCA9685()
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

servo_min = 150
servo_max = 600


class Servo:
    def __init__(self,iId,iPosition):
        self._id = iId
        self._position = iPosition

    def toDict(self):
        return {'id': self._id , 'position' : self._position }

    def fromDict(self, dict):
        self._id  = dict('id')
        self._position = dict('position')


    def move(self):
        aServoPosition = int((((self._position + 90.0) / 180.0) * (servo_max - servo_min)) + servo_min)

        print("Moving %d to position %d (servo position %d)" % (self._id,self._position,aServoPosition))

        if aServoPosition > servo_max:
            aServoPosition = servo_max

        if aServoPosition < servo_min:
            aServoPosition = servo_min

        pwm.set_pwm(self._id, 0, aServoPosition)

    def print2(self):
        print("Servo: _id: %d, _position: %d" % (self._id,self._position))
