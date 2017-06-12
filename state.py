
class State:

	def __init__(self, iServos):
		self._servos = iServos
	
	def addServo(self, iServo):
		self._servos.append(iServo)

	def move(self):
		for servo in self._servos:
			servo.move()
