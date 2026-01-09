from elevator_status import ElevatorStatus
from elevator_direction import ElevatorDirection
from elevator_curr_state import ElevatorCurrState
from controller_strategy.fcfs_elevator_control_strategy import FirstComeFirstServerElevatorControlStrategy

class ElevatorController:
    def __init__(self):
        self._state = ElevatorCurrState()
        self._control_strategy = None
    
    def set_curr_floor(self, floor_num):
        self._state.set_curr_floor(floor_num)
    
    def move_elevator_to_floor(self, floor_num):
        self._control_strategy = FirstComeFirstServerElevatorControlStrategy()

        next_stop = self._control_strategy.determine_next_stop(floor_num)


        #set direction based on next stop
        current_floor = self._state.curr_floor
        if next_stop > current_floor:
            self._state.curr_direction = ElevatorDirection.UP
        elif next_stop < current_floor:
            self._state.curr_direction = ElevatorDirection.DOWN
        
        if next_stop != current_floor:
            self._state.curr_status = ElevatorStatus.MOVING