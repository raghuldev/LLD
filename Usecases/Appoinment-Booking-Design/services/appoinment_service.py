from storage import APPOINMENTS
from models.appoinment import Appoinment
import uuid
class AppoinmentService:
    @staticmethod
    def create_appoinment(patient, slot):
        slot.book()
        appointment_id = str(uuid.uuid4())
        appoinment = Appoinment(appoinment_id=appointment_id, doctor=slot.doctor, patient=patient, slot=slot)
        APPOINMENTS[appointment_id] = appoinment
        return appoinment
    
    @staticmethod
    def cancel_appoinment(appoinment_id):
        appoinment = APPOINMENTS.pop(appoinment_id)
        print(f"Appointment for Patient {appoinment.patient.name} cancelled")
        appoinment.slot.free()
        
    