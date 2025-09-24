from abc import ABC, abstractmethod

class ILogger(ABC):
    @abstractmethod
    def log(slef, msg) -> None:
        """Log the message"""
        pass