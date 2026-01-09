from abc import ABC, abstractmethod
from external_request.external_request import ExternalRequest

class ElevatorSelectionStrategy(ABC):
    """Abstract base class for elevator selection strategies"""
    
    @abstractmethod
    def select_elevator(self, ext_req: ExternalRequest) -> int:
        pass
