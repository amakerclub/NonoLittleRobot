from servo import Servo
class State:

    def __init__(self, iServos):
        self._servos = iServos

    def toDict(self):
        return {'servos': self._servos.toDict() }

    def fromDict(self, dict):
        servos  = dict('servos')
        for servo in servos:
			self.addServo(self, Servo.fromDict(servo))

    def addServo(self, iServo):
        self._servos.append(iServo)

    def move(self):
        for servo in self._servos:
            servo.move()
