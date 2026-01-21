from commands.booking_commands import BookClassCommand, CancelClassCommand
from service.search_service import SearchService

class CultFitFacade:
    def book_class(self, user, class_session):
        return BookClassCommand(user, class_session).execute()
    def cancel_class(self, user, class_session):
        return CancelClassCommand(user, class_session).execute()
    def search_classes(self, center=None, class_type=None):
        return SearchService.search(center, class_type)
