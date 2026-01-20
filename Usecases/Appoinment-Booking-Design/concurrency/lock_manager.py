import threading

class SlotLockManager:
    _locks = {}
    _global_lock = threading.Lock()

    @classmethod
    def acquire(cls, slot_id):
        with cls._global_lock:
            if slot_id not in cls._locks:
                cls._locks[slot_id] = threading.Lock()
        cls._locks[slot_id].acquire()
    
    @classmethod
    def release(cls, slot_id):
        cls._locks[slot_id].release()