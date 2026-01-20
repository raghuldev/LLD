from command.commands import BookAppoinmentCommand, CancelAppointmentCommand
from services.search_service import SearchService

class AppointmentFacade:
    def book(self, patient, slot):
        return BookAppoinmentCommand(patient, slot).execute()
    
    def cancel(self, appointment_id):
        return CancelAppointmentCommand(appointment_id).execute()
    
    def search(self, specialty, sorting_strategy):
        return SearchService().search(specialty, sorting_strategy)