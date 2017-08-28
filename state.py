import json
from servo import Servo
class State:
    """a State is a set of (positions of) servos"""
    def __init__(self, iServos):
        self._servos = iServos

    def toDict(self):
        s=[]
        for servo in self._servos:
            s.append(servo.toDict())
        return {'servos': s }

    def fromDict(self, dict):
        servos  = dict('servos')
        for servo in servos:
			self.addServo(self, Servo.fromDict(servo))

    def addServo(self, iServo):
        self._servos.append(iServo)
