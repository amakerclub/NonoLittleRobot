# Import the PCA9685 module.
import Adafruit_PCA9685
import time
import logging

logger = logging.getLogger(__name__)

import gpioController

pwm = Adafruit_PCA9685.PCA9685() #FIXME Can this be moved inside the Executor class or be injected as dependency?
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

servo_min = 150
servo_max = 600


class Executor:
    """Executor is in charge of executing a movement, and getting its score."""

    def __init__(self, sleepTime=0):
        self._sleepTime=sleepTime

    def run(self, movement):
        """
        Physical execution of movement
        :param Move movement: Movement to be executed
        """
        for state in movement.states:
            for servo in state.servos:
                aServoPosition = int((((servo.position + 90.0) / 180.0) * (servo_max - servo_min)) + servo_min)
                logger.debug("Moving %d to position %d (servo position %d)" % (servo.id, servo.position, aServoPosition))
                
                if aServoPosition > servo_max:
                    aServoPosition = servo_max

                if aServoPosition < servo_min:
                    aServoPosition = servo_min

                pwm.set_pwm(servo.id, 0, aServoPosition)
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
