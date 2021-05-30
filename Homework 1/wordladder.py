from os import PathLike
from search import *

# Other functions
WORDS = set(i.lower().strip() for i in open('word.txt'))
def is_valid_word(word):
    return word in WORDS

# Defining the problem
class WordLadderProblem(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal=goal)

    def actions(self,state):
        actions_list = []
        # For each character in the word, it can be replaced with any other of the 25 letters
        for i in range(len(state)):
            for x in ALPHABET.lower():
                if is_valid_word(state[:i]+x+state[i+1:]) and x!= state[i]:
                    actions_list.append(state[:i]+x+state[i+1:])
        return actions_list
    
    # Choosing the action to replace the letter just yields the action in the word
    def result(self,state,action):
        return action

    # Check if the state is equals to the goal
    def goal_test(self, state):
        return super().goal_test(state)

    # Each change in letter is defined as cost = 1
    def path_cost(self, c, state1, action, state2):
        return super().path_cost(c, state1, action, state2)
    
    # Heuristic function to see if we are getting nearer or further from the word
    def h(self,node):
        cost=0
        for i in range(len(node.state)):
            if node.state[i] != self.goal[i]:
                cost +=1
        return cost

# Breadth first search works only for easier cases, and takes too long/takes up too much memory for other cases like wheat to bread, or stone to money
print("BFS for cold to warm")
path = breadth_first_tree_search(WordLadderProblem("cold","warm")).path()
for i in path:
    print(i)

print()

# Astar search on the other hand works very well even for the harder cases
print("Astar search for wheat to bread")
path = astar_search(WordLadderProblem("wheat","bread")).path()
for i in path:
    print(i)

print()
print("Astar search for stone to money")
path = astar_search(WordLadderProblem("stone","money")).path()
for i in path:
    print(i)