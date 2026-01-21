from service.booking_service import BookingService
from concurrency.lock_manager import LockManager
class Command:
    def execute(self):
        raise NotImplementedError


class BookClassCommand(Command):
    def __init__(self, user, class_session):
        self.user = user
        self.class_session = class_session
    
    def execute(self):
        user_lock = f"User_{self.user.user_id}"
        session_lock = f"Session_{self.class_session.id}"
        LockManager.acquire(user_lock)
        try:
            if BookingService.has_time_conflict(self.user, self.class_session):
                return f"Booking Rejected for {self.user.name} due to time overlap"
            LockManager.acquire(session_lock)
            try:
                if not self.class_session.is_full():
                    booking = BookingService.create_booking(self.user, self.class_session)
                    return f"Booking Confirmed for {booking.user.name}"
                else:
                    self.class_session.waitlist.append(self.user)
                    return f"{self.user.name} is added to waitlist!"
            finally:
                LockManager.release(session_lock)
        finally:
            LockManager.release(user_lock)

class CancelClassCommand(Command):
    def __init__(self, user, class_session):
        self.user = user
        self.class_session = class_session
    
    def execute(self):
        LockManager.acquire(self.class_session.id)
        try:
            BookingService.cancel_booking(self.user, self.class_session)
            return f"Booking Cancelled for {self.user.name}"
        finally:
            LockManager.release(self.class_session.id)
        