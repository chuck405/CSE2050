# This file empty on purpose - add the correct classes/methods below

class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority and self.item == other.item

class PQ_UL:
    def __init__(self):
        self._L = []
    
    def __len__(self):
        return len(self._L)

    def insert(self, item, priority):
        self._L.append(Entry(item, priority))

    def find_min(self):
        min_prio_entry = self._L[0]
        for i in self._L:
            if i < min_prio_entry:
                min_prio_entry = i
        return min_prio_entry

    def remove_min(self):
        min_prio_entry = self._L[0]
        for i in self._L:
            if i < min_prio_entry:
                min_prio_entry = i
        return self._L.pop(self._L.index(min_prio_entry))

class PQ_OL:
    def __init__(self):
        self._L = []

    def __len__(self):
        return len(self._L)

    def insert(self, item, priority):
        self._L.append(Entry(item, priority))
        self._L.sort(key=lambda obj: obj.priority, reverse=True)

    def find_min(self):
        return self._L[-1]

    def remove_min(self):
        return self._L.pop(-1)