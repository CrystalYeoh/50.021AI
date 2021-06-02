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

    # Part 2
    def matches(self,city, time):
        return self.start_city == city and self.start_time >= time

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

# Formulate the problem
class FlightItineraryProblem(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal=goal)

    def actions(self,state):
        actions_list = []
        # For each flight in flightDB, if it matches, then it is added to action list
        for i in flightDB:
            if i.matches(state["city"],state["time"]):
                actions_list.append(i)
        return actions_list
    
    # Choosing the action will update the current time and current city
    def result(self,state,action):
        new_state = {"city":action.end_city,"time":action.end_time}
        return new_state

    # Check if the state is equals to the goal, and that we reach at an earlier time
    def goal_test(self, state):
        return state["city"] == self.goal["city"] and state["time"] <= self.goal["time"]

    # Cost is defined as time taken to reach another city
    def path_cost(self, c, state1, action, state2):
        return c + (state2["time"] - state1["time"])

def find_itinerary(start_city, start_time, end_city, deadline):
    return uniform_cost_search(FlightItineraryProblem({"city":start_city,"time":start_time},{"city":end_city,"time":deadline}))


# Run this test if you would like to know
def test1():
    node = find_itinerary('Rome',1,'Istanbul',10)
    if node != None:
        for i in node.path():
            print(i)
    else:
        print("No solution was found")

# Part 4
"""
i) Yes this strategy will find the path that arrives the soonest, given that we start at 1. This is because if a path can be found, it will be found at the lowest path cost with the increment findings.

ii) If we use this strategy to solve a shortest path with length 200, it should take about 2x calls of find_itinerary to find.

iii) Done below with function find_shortest_itinerary()

iv) Done below with function find_shortest_itinerary_optimized()
Since I am using the UCS, the path found by find_itinerary is already the shortest path within the deadline. Thus to find the shortest path, I only need to start with a big deadline. This results in only needing to call find_itinerary() once.


"""

def find_shortest_itinerary(start_city, start_time, end_city):
    i = 1
    while i>0:
        node = find_itinerary(start_city,start_time,end_city,start_time+i)
        if node != None:
            print("Path found at {}th call".format(i))
            return node
        else: 
            i+=1

# Run to test shortest itinerary function
def test2():
    node = find_shortest_itinerary('Rome',1,'Istanbul')
    if node != None:
        for i in node.path():
            print(i)
    else:
        print("No solution was found")

def find_shortest_itinerary_optimized(start_city,start_time,end_city):
    return find_itinerary(start_city,start_time,end_city,sys.maxsize)

# Run to test shortest itinerary function optimized
def test3():
    node = find_shortest_itinerary_optimized('Rome',1,'Istanbul')
    if node != None:
        for i in node.path():
            print(i)
    else:
        print("No solution was found")


