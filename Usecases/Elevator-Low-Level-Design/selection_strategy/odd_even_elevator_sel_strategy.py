from selection_strategy.elevator_selection_strategy import ElevatorSelectionStrategy
from external_request.external_request import ExternalRequest

class OddEvenElevatorSelStrategy(ElevatorSelectionStrategy):
    def select_elevator(self, ext_req: ExternalRequest) -> int:  # ✅ self + return type
        if ext_req.src_floor % 2 == 1:
            return 1
        return 2
