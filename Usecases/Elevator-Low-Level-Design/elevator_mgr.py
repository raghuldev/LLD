from typing import Dict
from elevator import Elevator


class ElevatorMgr:
    _elevator_mgr_instance = None
    _elevators: Dict[int, 'Elevator'] = None

    def __new__(cls):
        """Singleton Implementation using __new__"""
        if cls._elevator_mgr_instance is None:
            cls._elevator_mgr_instance = super().__new__(cls)
        return cls._elevator_mgr_instance
    
    def __init__(self):
        """Private contructor - only called for singleton"""
        if self._elevators is not None:
            return #Already initialized
        self._elevators = {}
    
    @classmethod
    def get_elevator_mgr(cls):
        if cls._elevator_mgr_instance is None:
            cls._elevator_mgr_instance = cls()
        return cls._elevator_mgr_instance
    
    def initialize_elevators(self, noOfElevators):
        for i in range(1, noOfElevators+1):
            self._elevators[i] = Elevator()
    
    def get_elevator(self, elevatorId):
        return self._elevators.get(elevatorId)