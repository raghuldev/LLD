from elevator_direction import ElevatorDirection
from elevator_status import ElevatorStatus
class ElevatorCurrState:
    def __init__(self):
        self._curr_floor = 0
        self._curr_direction = ElevatorDirection.IDLE
        self._curr_status = ElevatorStatus.IDLE
    
    @property
    def curr_floor(self):
        """Get Current Floor"""
        return self._curr_floor
    
    @curr_floor.setter
    def curr_floor(self, floor_num):
        """Set Current Floor"""
        self._curr_floor = floor_num

    
    @property
    def curr_direction(self):
        """Get Current Direction"""
        return self._curr_direction
    
    @curr_direction.setter
    def curr_direction(self, direction):
        """Set Current Direction"""
        self._curr_direction = direction
    

    @property
    def curr_status(self):
        """Get Current Status"""
        return self._curr_status
    
    @curr_status.setter
    def curr_status(self, status):
        """Set CUrrent Status"""
        self._curr_status = status