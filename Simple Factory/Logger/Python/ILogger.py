from abc import ABC, abstractmethod

class ILogger(ABC):
    @abstractmethod
    def log(self, msg) -> None:
        """Log the message"""
        pass