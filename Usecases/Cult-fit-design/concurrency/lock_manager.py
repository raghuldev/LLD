import threading

class LockManager:
    _locks = {}
    _global_lock = threading.Lock()

    @classmethod
    def acquire(cls, key):
        with cls._global_lock:
            if key not in cls._locks:
                cls._locks[key] = threading.Lock()
        cls._locks[key].acquire()
    
    @classmethod
    def release(cls, key):
        cls._locks[key].release()