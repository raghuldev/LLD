from concurrency.lock_manager import SlotLockManager
from services.appoinment_service import AppoinmentService
from models.booking_result import BookingResult

class Command:
    def execute(self):
        raise NotImplementedError
    

class BookAppoinmentCommand(Command):
    def __init__(self, patient, slot):
        self.patient = patient
        self.slot = slot
        
    def execute(self):
        SlotLockManager.acquire(self.slot.slot_id)
        
        try:
            if self.slot.is_free():
                appointment = AppoinmentService.create_appoinment(self.patient, self.slot)
                return BookingResult(success=True, message= f"Booking Confirmed for {self.patient.name}", appointment=appointment)
            else:
                self.slot.waitlist.add(self.patient)
                # print(f"HIIIII >>>>>> {self.slot.waitlist.poll()}")
                return BookingResult(
                    success=False,
                    message=f"{self.patient.name} added to waitlist"
                )
        finally:
            SlotLockManager.release(self.slot.slot_id)

class CancelAppointmentCommand(Command):
    def __init__(self, appointment_id):
        self.appointment_id = appointment_id

    def execute(self):
        AppoinmentService().cancel_appoinment(self.appointment_id)