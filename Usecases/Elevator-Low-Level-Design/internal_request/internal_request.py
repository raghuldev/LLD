class InternlRequest:
    def __init__(self, dest_floor: int, src_elevator_id: int):
        self._dest_floor = dest_floor
        self._src_elevator_id = src_elevator_id
    
    @property
    def dest_floor(self):
        return self._dest_floor
    
    @dest_floor.setter
    def dest_floor(self, dest_floor):
        self._dest_floor = dest_floor
    
    @property
    def src_elevator_id(self):
        return self._src_elevator_id
    
    @src_elevator_id.setter
    def src_elevator_id(self, p_src_elevator_id: int):
        self._src_elevator_id = p_src_elevator_id