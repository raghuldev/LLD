from services.appoinment_service import AppoinmentService
class WaitlistObserver:
    def notify(self, slot):
        if not slot.waitlist.is_empty():
            patient = slot.waitlist.poll()
            # print(f"PATIENT FROM WAITLIST {patient}")
            # create appoinment for this patient
            AppoinmentService.create_appoinment(patient, slot)
            print(f"Patient {patient.name} is promoted to CONFIRMED!")
            # return BookingResult(success=True, message= f"Booking Confirmed for {patient.name}", appointment=appointment)