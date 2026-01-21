class Center:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.class_sessions = []
    
    def add_class(self, class_session):
        self.class_sessions.append(class_session)
        