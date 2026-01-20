class Doctor:
    def __init__(self, doctor_id, name, specialty, rating):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.rating = rating
        self.slots = []

    def add_slots(self, slot):
        self.slots.append(slot)
        