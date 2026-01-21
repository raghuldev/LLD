from collections import deque
class ClassSession:
    def __init__(self, id, type, center, start, end, capacity, trainer):
        self.id = id
        self.type = type
        self.center = center
        self.start = start
        self.end = end
        self.capacity = capacity
        self.trainer = trainer
        self.booked_users = set()
        self.waitlist = deque()
    
    def is_full(self):
        return len(self.booked_users) >= self.capacity
    
    def add_user(self, user):
        self.booked_users.add(user.user_id)
    
    def remove_user(self, user):
        self.booked_users.remove(user.user_id)