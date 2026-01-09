from elevator_direction import ElevatorDirection
class ExternalRequest:
    def __init__(self, direction: ElevatorDirection, floor: int):
        self._direction_to_go = direction
        self._src_floor = floor
    
    @property
    def direction(self):
        return self._direction_to_go
    
    @direction.setter
    def direction(self, direction: ElevatorDirection):
        self._direction_to_go = direction
    
    @property
    def src_floor(self):
        return self._src_floor
    
    @src_floor.setter
    def src_floor(self, floor: int):
        self.src_floor = floor