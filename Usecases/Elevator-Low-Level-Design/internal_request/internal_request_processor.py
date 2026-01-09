from elevator_mgr import ElevatorMgr
from internal_request.internal_request import InternlRequest

class InternalRequestProcessor:
    def process_internal_request(self, int_req: InternlRequest):
        elevator_mgr = ElevatorMgr.get_elevator_mgr()
        src_elevator = elevator_mgr.get_elevator(int_req.src_elevator_id)
        src_elevator.move_to_floor(int_req.dest_floor)