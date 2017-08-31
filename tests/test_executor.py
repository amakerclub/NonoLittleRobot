import unittest
from mock import Mock, call
from mock.mock import patch
from move import Move
from state import State
from servo import Servo

class TestExecutor(unittest.TestCase):
    def setUp(self):
        self._adafruit_mock = Mock()
        self._pwm = self._adafruit_mock.PCA9685.return_value = Mock()
        self._module_patcher = patch.dict('sys.modules', Adafruit_PCA9685=self._adafruit_mock)
        self._module_patcher.start()
        
    def tearDown(self):
        self._module_patcher.stop()
        
    def test_pca9685_is_initialized_with_60_mhz(self):
        from executor import Executor
        self._pwm.set_pwm_freq.assert_called_once_with(60)
        
    def test_set_pwm_is_not_called_when_movement_without_states(self):
        from executor import Executor
        exe = Executor()
        movement = Move([])
        exe.run(movement)
        self._pwm.set_pwm.assert_not_called()
        
    def test_set_pwm_is_not_called_when_states_without_servos(self):
        from executor import Executor
        exe = Executor()
        states = [State([])]
        movement = Move(states)
        exe.run(movement)
        self._pwm.set_pwm.assert_not_called()
        
    def test_set_pwm_is_called_with_the_value_of_the_servo(self):
        from executor import Executor
        exe = Executor()
        servos = [Servo(1, 80)]
        states = [State(servos)]
        movement = Move(states)
        exe.run(movement)
        self._pwm.set_pwm.assert_called_once_with(1, 0, 575)
        
    def test_that_position_stays_to_servo_max_when_limit_passed(self):
        from executor import Executor
        exe = Executor()
        servos = [Servo(1, 100)]
        states = [State(servos)]
        movement = Move(states)
        exe.run(movement)
        self._pwm.set_pwm.assert_called_once_with(1, 0, 600)
        
    def test_that_position_is_set_for_multiple_servos(self):
        from executor import Executor
        exe = Executor()
        servos = [Servo(1, 100), Servo(2, 80)]
        states = [State(servos)]
        movement = Move(states)
        exe.run(movement)
        self._pwm.set_pwm.assert_has_calls([
            call(1, 0, 600),
            call(2, 0, 575)
        ], any_order=False)

    def test_that_position_is_set_for_multiple_states_and_servos(self):
        from executor import Executor
        exe = Executor()
        servos1 = [Servo(1, 100), Servo(2, 80)]
        servos2 = [Servo(1, 50), Servo(2, 30)]
        states = [State(servos1), State(servos2)]
        movement = Move(states)
        exe.run(movement)
        self._pwm.set_pwm.assert_has_calls([
            call(1, 0, 600),
            call(2, 0, 575),
            call(1, 0, 500),
            call(2, 0, 450)
        ], any_order=False)

if __name__ == "__main__":
    unittest.main()