from search import *

class Flight:
    def __init__(self, start_city, start_time, end_city, end_time):
        self.start_city = start_city
        self.start_time = start_time
        self.end_city = end_city
        self.end_time = end_time
    def __str__(self):
        return str((self.start_city, self.start_time))+' -> '+str((self.end_city,self.end_time))
    
    __repr__ = __str__

    def matches(self,city, time):
        return self.start_city == city and self.time >= time

flightDB = [Flight('Rome', 1, 'Paris', 4),
Flight('Rome', 3, 'Madrid', 5),
Flight('Rome', 5, 'Istanbul', 10),
Flight('Paris', 2, 'London', 4),
Flight('Paris', 5, 'Oslo', 7),
Flight('Paris', 5, 'Istanbul', 9),
Flight('Madrid', 7, 'Rabat', 10),
Flight('Madrid', 8, 'London', 10),
Flight('Istanbul', 10, 'Constantinople', 10)]

# Part 1
"""
A good choice of state would be the current city and current time. Because we want the state to represent a physical configuration of the current, instead of the goal such as destination city or deadline, since those are constants.
"""

# Part 2
"""
Added in above
"""

# Part 3
def find_itinerary(self,):
    pass