"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Main Auth: Tanmay B.

Mean Window FP Filter (False Positive Filter)

- New detection pushed into window
- old entry popped
- mean found
- replace all self.aruco_detected conditions with the mean_window technique
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Links:
https://docs.python.org/3/library/collections.html#collections.deque
https://realpython.com/python-deque/
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

from collections import deque

class mean_window():
    def __init__(self, window_size):
        self.window_size = window_size
        self.window  = deque()

        for i in range(self.window_size):
            self.window.append(0)

    def update_and_get_activation(self, new_entry):
        self.window.popleft()
        self.window.append(new_entry)
        return self.find_activation()
    
    def find_activation(self):
        num = self.window.count(1)
        activation = float(num)/float(self.window_size)
        return activation
    
    def reg_time(self, time):
        self.registered_time = time

    def is_timeout(self, time, threshold):
        if self.registered_time is not None:
            detection_time = time - self.registered_time
            if detection_time >= threshold:
                return True
            return False
        else:
            return False