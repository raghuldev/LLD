class SlotSortingStrategy:
    def sort(self, slots):
        raise NotImplementedError
    
class SortByTime(SlotSortingStrategy):
    def sort(self, slots):
        return sorted(slots, key=lambda s: s.start)

class SortByRating(SlotSortingStrategy):
    def sort(self, slots):
        return sorted(slots, key=lambda s: s.doctor.rating, reverse=True)