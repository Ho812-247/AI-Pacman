# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    
  
    frontier = util.Stack()
    explored = set()
    start_state = problem.getStartState()
    frontier.push((start_state, []))  # Push initial state with empty path

    while not frontier.isEmpty():
        current_state, path = frontier.pop()

        if problem.isGoalState(current_state):
            return path

        explored.add(current_state)

        for successor, action, stepCost in problem.getSuccessors(current_state):
            if successor not in explored:
                frontier.push((successor, path + [action]))

    return []  # No path found
    util.raiseNotDefined()

def breadthFirstSearch(problem):
   
    """Search the shallowest nodes in the search tree first."""
    node = (problem.getStartState(), [], 0)  # (state, path, cost)
    if problem.isGoalState(node[0]):
        return node[1]

    frontier = util.Queue()
    frontier.push(node)
    explored = set()

    while not frontier.isEmpty():
        node = frontier.pop()
        state, path, cost = node

        if state in explored:
            continue
        explored.add(state)

        if problem.isGoalState(state):
            return path

        for successor, action, stepCost in problem.getSuccessors(state):
            child_node = (successor, path + [action], cost + stepCost)  # Include cost (not used in BFS but good practice)
            if successor not in explored: # Check is performed when popping
                frontier.push(child_node)
    
    return []  # No path found
    util.raiseNotDefined()

def uniformCostSearch(problem):
   
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()
    explored = set()
    start_state = problem.getStartState()
    frontier.push((start_state, [], 0), 0)  # (state, path, cost), priority

    while not frontier.isEmpty():
        current_state, path, cost = frontier.pop()

        if current_state in explored:
            continue  # Skip already explored nodes
        explored.add(current_state)


        if problem.isGoalState(current_state):
            return path

        for successor, action, stepCost in problem.getSuccessors(current_state):
            new_cost = cost + stepCost
            frontier.push((successor, path + [action], new_cost), new_cost)  # Priority = cost

    return [] # No path found
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    frontier = util.PriorityQueue()
    explored = set()
    start_state = problem.getStartState()
    frontier.push((start_state, [], 0), heuristic(start_state, problem)) # (state, path, cost), priority

    while not frontier.isEmpty():
        current_state, path, cost = frontier.pop()

        if current_state in explored:
            continue
        explored.add(current_state)

        if problem.isGoalState(current_state):
            return path

        for successor, action, stepCost in problem.getSuccessors(current_state):
            new_cost = cost + stepCost
            new_path = path + [action]
            priority = new_cost + heuristic(successor, problem)  # f(n) = g(n) + h(n)
            frontier.push((successor, new_path, new_cost), priority)

    return []  # No path found
    util.raiseNotDefined()

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

# ... (Other functions and classes remain the same)

def bestFirstSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest heuristic first."""
    frontier = util.PriorityQueue()
    explored = set()
    start_state = problem.getStartState()
    frontier.push((start_state, []), heuristic(start_state, problem))  # (state, path), priority

    while not frontier.isEmpty():
        current_state, path = frontier.pop()

        if current_state in explored:
            continue
        explored.add(current_state)

        if problem.isGoalState(current_state):
            return path

        for successor, action, stepCost in problem.getSuccessors(current_state):
            new_path = path + [action]
            priority = heuristic(successor, problem)  # Use heuristic for priority
            frontier.push((successor, new_path), priority)

    return []  # No path found
    util.raiseNotDefined()
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
befs = bestFirstSearch