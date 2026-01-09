from abc import ABC, abstractmethod

class ElevatorControlStrategy(ABC):
    """Abstarct Class for elevator control strategy"""

    @abstractmethod
    def determine_next_stop(self, floor_num: int) -> int:
        """
        Determine the next stop floor based on current requests
        
        Args:
            floor_num: Target floor number
        Returns:
            int: Next stop floor
        """
        pass