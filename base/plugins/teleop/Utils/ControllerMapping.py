__author__ = "Joshua Nelson"
__copyright__ = "Copyright 2022, R3 - Ryerson RAMS Robotics"
__credits__ = ["Joshua Nelson"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Joshua Nelson"
__status__ = "Done"


class Mapping:
    def __init__(self, b1: int, b2: int, b3: int, b4: int, l1: int, r1: int, lb: int, rb: int, back: int, start: int,
                 home: int, dUp: int, dDown: int, dLeft: int, dRight: int):
        self.BTN1 = b1
        self.BTN2 = b2
        self.BTN3 = b3
        self.BTN4 = b4
        self.BTNL1 = l1
        self.BTNR1 = r1
        self.BTNLB = lb
        self.BTNRB = rb
        self.BTNBACK = back
        self.BTNSTART = start
        self.BTNHOME = home
        self.BTNDUP = dUp
        self.BTNDDOWN = dDown
        self.BTNDLEFT = dLeft
        self.BTNDRIGHT = dRight
