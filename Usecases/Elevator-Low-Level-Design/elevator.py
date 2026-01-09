from elevator_controller import ElevatorController
class Elevator:
    def __init__(self):
        self._elevator_id = None
        self._controller = ElevatorController()
    
    @property
    def elevator_id(self):
        return self._elevator_id
    
    @elevator_id.setter
    def elevator_id(self, elevator_id):
        """Setter for elevator_id"""
        self._elevator_id = elevator_id
    

    def move_to_floor(self, floor_num):
        """Move elevator to specfic floor"""
        self._controller.move_elevator_to_floor(floor_num)
    
    def notify_floor_num_update(self, floor_num):
        self._controller.set_curr_floor(floor_num)