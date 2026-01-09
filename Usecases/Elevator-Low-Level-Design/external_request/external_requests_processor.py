from selection_strategy.odd_even_elevator_sel_strategy import OddEvenElevatorSelStrategy
from external_request.external_request import ExternalRequest
from elevator_mgr import ElevatorMgr

class ExternalRequestProcessor:
    def __init__(self):
        self._elevator_selection_strategy = OddEvenElevatorSelStrategy()

    def set_elevator_selection_strategy(self, selection_strategy):
        self._elevator_selection_strategy = selection_strategy
    

    def process_external_request(self, ext_req: ExternalRequest):
        assigned_elevator_id = self._elevator_selection_strategy.select_elevator(ext_req)

        elevator_mgr = ElevatorMgr.get_elevator_mgr()
        assigned_elevator = elevator_mgr.get_elevator(assigned_elevator_id)
        assigned_elevator.move_to_floor(ext_req.src_floor)