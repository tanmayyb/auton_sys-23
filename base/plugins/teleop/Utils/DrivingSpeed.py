__author__ = "Joshua Nelson"
__copyright__ = "Copyright 2022, R3 - Ryerson RAMS Robotics"
__credits__ = ["Joshua Nelson"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Joshua Nelson"
__status__ = "Done"


def _errorCheck(speed: float):
    if speed > 1 or speed < 0:
        print("Error - DRIVING SPEED is out of bounds\nAborting...")
        exit(1)


class DrivingSpeed:
    _speed: float
    _modifier = 0.1  # changes how quickly the speed will increase/decrease
    _revModifier = 0.2  # changes how quickly the speed will increase/decrease during a 'rev'

    _threshold = 25
    _current = 0

    def __init__(self, initialSpeed: float):
        # error check
        _errorCheck(initialSpeed)
        self._speed = initialSpeed

    def setSpeed(self, speed: float):
        # error check
        _errorCheck(speed)
        self._speed = speed

    def speed(self) -> float:
        return self._speed

    def gearUp(self):
        """
        Increases the speed by a fixed amount
        :return:
        """
        if self._speed + self._modifier <= 1:
            self._speed += self._modifier
        else:
            self._speed = 1

    def gearDown(self):
        """
        Decreases the speed by a fixed amount
        :return:
        """
        if self._speed - self._modifier >= 0:
            self._speed -= self._modifier
        else:
            self._speed = 0

    def revUp(self):
        """
        Revs Up the speed
        :return:
        """
        if self._speed + self._modifier * self._revModifier <= 1:
            if self._rev():
                self._speed += self._modifier * self._revModifier
        else:
            self._speed = 1

    def revDown(self):
        """
        Revs down the speed
        :return:
        """
        if self._speed - self._modifier * self._revModifier >= 0:
            if self._rev():
                self._speed -= self._modifier * self._revModifier
        else:
            self._speed = 0

    def _rev(self) -> bool:
        """
        Acts as a 'timer' for the rev functions
        :return:
        """
        self._current += 1
        if self._current >= self._threshold:
            self._current = 0
            return True
        return False
