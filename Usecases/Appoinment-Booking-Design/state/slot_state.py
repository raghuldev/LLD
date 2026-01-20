class SlotState:
    def book(self, slot):
        raise NotImplementedError
    
    def free(self, slot):
        raise NotImplementedError


class FreeState(SlotState):
    def book(self, slot):
        slot.state = BookedState()
    
    def free(self, slot):
        pass

class BookedState(SlotState):
    def book(self, slot):
        raise Exception("Slot Already booked")
    
    def free(self, slot):
        slot.state = FreeState()