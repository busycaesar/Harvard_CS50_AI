import sys

class Node():
    def __init__(self, state, parent, action):
        # Each node is keeping track of its current state, the state before the state (parent state), and the action.
        # In this case we are not keeping track of the path cost, as it can be calculated at the end when as reach from the initial state to the goal.
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
