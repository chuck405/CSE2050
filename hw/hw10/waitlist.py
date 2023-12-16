import random
class Time:
    """A class that represents time in the format HH:MM"""
    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)

    def __lt__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self < other, and False otherwise"""
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False
    
    def __eq__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self == other, and False otherwise"""
        if self.hour ==  other.hour and self.minute == other.minute:
            return True
        else:
            return False

    def __repr__(self):
        """Return the string representation of the time"""
        return f"{self.hour:02d}:{self.minute:02d}"

class Entry:
    """A class that represents a customer in the waitlist"""
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __lt__(self, other):
        """Compare two customers based on their time, if equal then compare based on the customer name"""
        if self.time == other.time:
            return self.name < other.name
        return self.time < other.time
    

class Waitlist:
    def __init__(self):
        self._entries = []

    def add_customer(self, item, priority):
        """Adds customers to the waiting list"""
        # checks if the time is valid, then appends and upheaps
        if priority.hour in range(00,24) and priority.minute in range(00,60):
            self._entries.append(Entry(item, priority))
            self._upheap(len(self._entries)-1)

    def peek(self):
        """Peeks and sees the first customer in the waitlist (i.e., the customer with the highest priority)"""
        # returns a tuple of the extracted item (customer, time), return None if the heap is empty
        if len(self._entries) == 0: return None
        else: return (self._entries[0].name, self._entries[0].time)

    def seat_customer(self):
        """Extracts the customer with the highest priority (i.e., the earliest reservation time) from the priority queue"""
        # removes the first customer and downheaps
        L = self._entries
        item = L[0]
        L[0] = L[-1]
        L.pop()
        self._downheap(0)
        # returns a tuple of the extracted item (customer, time)
        return (item.name, item.time)

    def print_reservation_list(self):
        """Prints all customers in order of their priority (reservation time)"""
        # maintains the heap property by copying the waitlist and repeatedly performing seat_customer() on the copy
        WL_copy = Waitlist()
        WL_copy._entries = self._entries[:]
        for i in WL_copy._entries:
            next_customer = WL_copy.seat_customer()
            print("The next customer on the waitlist is: " + str(next_customer[0]) + ", time: " + str(next_customer[1]))
    
    def change_reservation(self, name, new_priority):
        """Changes the reservation time (priority) for the customer with the given name"""
        # checks if the new time is valid
        if new_priority.hour in range(00,24) and new_priority.minute in range(0,60):
            # finds the entry whose name matches
            for i in self._entries:
                if i.name == name:
                    # returns if the new time is the same
                    if i.time == new_priority: return
                    # updates and upheaps if the new time is earlier
                    elif i.time > new_priority:
                        i.time = new_priority
                        self._upheap(self._entries.index(i))
                    # updates and downheaps if the new time is later
                    else: 
                        i.time = new_priority
                        self._downheap(self._entries.index(i))
        
    def _parent(self, i):
        """Method to assist in heap ordering"""
        return (i - 1) // 2

    def _children(self, i):
        """Method to assist in heap ordering"""
        left = 2 * i + 1
        right = 2 * i + 2
        return range(left, min(len(self._entries), right + 1))
    
    def _upheap(self, i):
        """Method to assist in heap ordering"""
        L = self._entries
        parent = self._parent(i)
        if i > 0 and L[i] < L[parent]:
            self._swap(i, parent)
            self._upheap(parent)

    def _downheap(self, i):
        """Method to assist in heap ordering"""
        L = self._entries
        children = self._children(i)
        if children:
            child = min(children, key = lambda x: L[x])
            if L[child] < L[i]:
                self._swap(i, child)
                self._downheap(child)
    
    def _swap(self, a, b):
        """Method to assist in heap ordering"""
        L = self._entries
        L[a], L[b] = L[b], L[a]