from models.class_session import ClassSession
from models.user import User
import uuid
from storage import BOOKINGS, USER_BOOKING
from models.booking import Booking

class BookingService:
    @staticmethod
    def has_time_conflict(user, new_session):
        sessions = USER_BOOKING.get(user.user_id, [])
        for session in sessions:
            if not (session.start >= new_session.end or session.end <= new_session.start):
                return True
        return False
    
    @staticmethod
    def create_booking(user, class_session):
        USER_BOOKING.setdefault(user.user_id, []).append(class_session)
        class_session.add_user(user)
        booking_id = str(uuid.uuid4())
        booking = Booking(booking_id, user, class_session)
        BOOKINGS[booking_id] = booking
        return BOOKINGS[booking_id]
    
    @staticmethod
    def cancel_booking(user, class_session):
        class_session.remove_user(user)
        USER_BOOKING[user.user_id].remove(class_session)
        print(f"Booking for {user.name} cancelled Successfully")
        if class_session.waitlist:
            next_user = class_session.waitlist.popleft()
            class_session.add_user(next_user)
            print(f"From Waitlist {next_user.name} has promoted for booking!")