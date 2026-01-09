from elevator_mgr import ElevatorMgr
from external_request.external_requests_processor import ExternalRequestProcessor
from internal_request.internal_request_processor import InternalRequestProcessor
from external_request.external_request import ExternalRequest
from internal_request.internal_request import InternlRequest

class ElevatorSystem:
    _instance = None
    _no_of_floors = 0
    _no_of_elevators = 0
    _ext_req_processor = None
    _int_req_processor = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ElevatorSystem, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if hasattr(self, '_initialized'):
            return
        self._initialized = True
    
    @classmethod
    def get_elevator_system(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def initialize_elevator_system(self, pNoOfFloors, pNoOfElevators):
        self._no_of_floors = pNoOfFloors
        self._no_of_elevators = pNoOfElevators

        print(f"Initialized elevator system with {self._no_of_floors} floors and {self._no_of_elevators} elevators")

        #initalizig elevator Manager

        elevatorMgr = ElevatorMgr.get_elevator_mgr()
        elevatorMgr.initialize_elevators(self._no_of_elevators)

        self._ext_req_processor = ExternalRequestProcessor()
        self._int_req_processor = InternalRequestProcessor()
    
    def set_elevator_selectionStrategy(self, selectionStrategy):
        if self._ext_req_processor:
            self._ext_req_processor.set_elevator_selection_strategy(selectionStrategy)
    
    def send_external_request(self, direction, srcFloor):
        if self._ext_req_processor:
            self._ext_req_processor.process_external_request(ExternalRequest(direction, srcFloor))
    
    def send_internal_request(self, destFloor, elevatorId):
        if self._int_req_processor:
            self._int_req_processor.process_internal_request(InternlRequest(destFloor, elevatorId))