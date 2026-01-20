from storage import DOCTORS
class SearchService:
    def search(self, specialty, sorting_strtegy):
        slots =[]
        for doctor in DOCTORS.values():
            if doctor.specialty == specialty:
                for slot in doctor.slots:
                    if slot.is_free():
                        slots.append(slot)
        return sorting_strtegy.sort(slots)