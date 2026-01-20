from state.slot_state import FreeState
from collections import deque

class Waitlist:
    def __init__(self):
        self.queue = deque()
    
    def add(self, patient):
        # print(f"Added patient {patient.name} to Queue!!")
        self.queue.append(patient)
        # print(f"Current Queue >>> {self.queue}")
    
    def poll(self):
        # print(f"Current POLL Queue >>> {self.queue}")
        return self.queue.popleft() if self.queue else None
    
    def is_empty(self):
        return len(self.queue) == 0


class TimeSlot:
    def __init__(self, slot_id, doctor, start, end):
        self.slot_id = slot_id
        self.doctor = doctor
        self.start = start
        self.end = end
        self.state = FreeState()
        self.waitlist = Waitlist()
        self.observers = []
    
    def is_free(self):
        return isinstance(self.state, FreeState)
    
    def book(self):
        self.state.book(self)
    
    def free(self):
        self.state.free(self)
        self.notify()
    
    def attach(self, observer):
        self.observers.append(observer)
    
    def notify(self):
        for obs in self.observers:
            obs.notify(self)
