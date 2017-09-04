

# Import the PCA9685 module.
import Adafruit_PCA9685
import time


import gpioController


pwm = Adafruit_PCA9685.PCA9685()
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

servo_min = 150
servo_max = 600


class Executor:
    """Executor is in charge of executing a movement, and getting its score."""

    def __init__(self, sleepTime):
        self._sleepTime=sleepTime

    def run(self, movement):
        """Physical executio of movement"""
        for state in movement.states:
            for servo in state._servos:
                aServoPosition = int((((servo._position + 90.0) / 180.0) * (servo_max - servo_min)) + servo_min)
                print("Moving %d to position %d (servo position %d)" % (self._id,self._position,aServoPosition))
                if aServoPosition > servo_max:
                    aServoPosition = servo_max

                if aServoPosition < servo_min:
                    aServoPosition = servo_min

                pwm.set_pwm(self._id, 0, aServoPosition)
            time.sleep(self._sleepTime)
        #TODO : update movement with its score

        try:

            print ("First measure...")
            dist = gpioController.calculateDistance()
            print ("Done")
            time.sleep(1)
            print ("Avg. measure...")
            distAvg = gpioController.calculateAverageDistance(10,1)
            print ("Done")
            print ("Measured Distance = %.1f cm (%.1f cm)" % (dist,distAvg))
            time.sleep(1)
            return distAvg

            # Reset by pressing CTRL + C
        except KeyboardInterrupt:
            print("Measurement stopped by User")
        #GPIO.cleanup()
