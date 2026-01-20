from models.doctor import Doctor
from models.slot import TimeSlot
from models.patient import Patient
from enums import Speciality
from datetime import datetime, timedelta
from observer.waitlist_observer import WaitlistObserver
from storage import DOCTORS, PATIENTS
from facade.appointment_facade import AppointmentFacade
from strategy.slot_sorting import SortByTime

doc1 = Doctor("D1", "RAGHUL", Speciality.CARDIOLOGIST, 4.9)

slot1 = TimeSlot("S1", doc1, datetime.now(), datetime.now() + timedelta(minutes=30))
slot1.attach(WaitlistObserver())
doc1.add_slots(slot1)

DOCTORS[doc1.doctor_id] = doc1

p1 = Patient("P1", "RAAM")
p2 = Patient("P2", "ABC")

PATIENTS[p1.patient_id] = p1
PATIENTS[p2.patient_id] = p2

facade = AppointmentFacade()

slots = facade.search(Speciality.CARDIOLOGIST, SortByTime())

print(f"Available Slots : {[s.slot_id for s in slots]}")

res1 = facade.book(p1, slot1)
print(res1.message)

res2 = facade.book(p2, slot1)
print(res2.message)

facade.cancel(res1.appointment.appoinment_id)
