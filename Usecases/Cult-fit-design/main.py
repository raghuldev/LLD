from enums import ClassType
from models.user import User
from models.trainer import Trainer
from models.center import Center
from models.class_session import ClassSession
from models.booking import Booking
from datetime import datetime, timedelta
from facade.cult_fit_facade import CultFitFacade
from storage import CENTERS

c1 = Center("C1", "KORAMANGALA_FIT")

trainer1 = Trainer("T1", "RAGHUL", "DANCE", 4.9)
trainer2 = Trainer("T2", "Coach1", "BOXING", 4.5)

session1 = ClassSession("S1", ClassType.DANCE, c1, datetime.now(), datetime.now() + timedelta(minutes=30), 1, trainer1)
session2 = ClassSession("S2", ClassType.BOXING, c1, datetime.now() + timedelta(minutes=15), datetime.now() + timedelta(minutes=45), 1, trainer2)

c1.add_class(session1)
c1.add_class(session2)
CENTERS["C1"] = c1
user1 = User("U1", "RAAM")
user2 = User("U2", "Bob")

facade = CultFitFacade()

print(facade.book_class(user1, session1))
print(facade.book_class(user1, session2))
print(facade.book_class(user2, session1))
facade.cancel_class(user1, session1)

for cls in facade.search_classes("C1"):
    print(f"{cls.id}")