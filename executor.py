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

        try:
            print ("Measure distance before moving")
            avgDistBefore = gpioController.calculateAverageDistance(4,0.1)
            print avgDistBefore

        # Reset by pressing CTRL + C
        except KeyboardInterrupt:
            print("Measurement stopped by User")


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

        try:
            print ("Measure distance after moving")
            avgDistAfter = gpioController.calculateAverageDistance(4,0.1)
            print avgDistAfter

        # Reset by pressing CTRL + C
        except KeyboardInterrupt:
            print("Measurement stopped by User")

        print (avgDistAfter - avgDistBefore)

        return (avgDistAfter - avgDistBefore)

        #GPIO.cleanup()
