class BookingResult:
    def __init__(self, success, message, appointment = None):
        self.success = success
        self.message = message
        self.appointment = appointment