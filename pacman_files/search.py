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
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    "*** YOUR CODE HERE ***"

    state = problem.getStartState()
    starting_state = state
    if(problem.isGoalState(state)):
        return []
    dictNode = {}
    frontier = util.Stack()
    dictNode[state] = ('Stop', None)
    dictNode['Last Node'] = state
    frontier.push(dictNode)
    explored = set()
    ActionsList = []
    while(True):
        if(frontier.isEmpty()):
            return []
        current_DictNode = frontier.pop()
        explored.add(current_DictNode['Last Node'])
        for child in problem.getSuccessors(current_DictNode['Last Node']):
            if(child[0] not in explored):
                if(problem.isGoalState(child[0])):
                    current_DictNode[child[0]] = (current_DictNode['Last Node'], child[1])
                    current_DictNode['Last Node'] = child[0]
                    tmpNode = current_DictNode[child[0]]
                    ActionsList.append(tmpNode[1])
                    while True:
                        if(tmpNode[0] == starting_state):
                            break
                        tmpNode = current_DictNode[tmpNode[0]]
                        ActionsList.append(tmpNode[1])
                    ActionsList.reverse()
                    return ActionsList
                newDictNode = current_DictNode.copy()
                newDictNode[child[0]] = (newDictNode['Last Node'], child[1])
                newDictNode['Last Node'] = child[0]
                frontier.push(newDictNode)
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    state = problem.getStartState()
    starting_state = state
    if(problem.isGoalState(state)):
        return []
    dictNode = {}
    frontier = util.Queue()
    dictNode[state] = ('Stop', None)
    dictNode['Last Node'] = state
    frontier.push(dictNode)
    explored = set()
    ActionsList = []
    while(True):
        if(frontier.isEmpty()):
            return []
        current_DictNode = frontier.pop()
        explored.add(current_DictNode['Last Node'])
        for child in problem.getSuccessors(current_DictNode['Last Node']):
            if(child[0] not in explored):
                if(problem.isGoalState(child[0])):
                    current_DictNode[child[0]] = (
                        current_DictNode['Last Node'], child[1])
                    current_DictNode['Last Node'] = child[0]
                    tmpNode = current_DictNode[child[0]]
                    ActionsList.append(tmpNode[1])
                    while True:
                        if(tmpNode[0] == starting_state):
                            break
                        tmpNode = current_DictNode[tmpNode[0]]
                        ActionsList.append(tmpNode[1])
                    ActionsList.reverse()
                    return ActionsList
                newDictNode = current_DictNode.copy()
                newDictNode[child[0]] = (newDictNode['Last Node'], child[1])
                newDictNode['Last Node'] = child[0]
                frontier.push(newDictNode)

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    state = problem.getStartState()
    frontier = util.PriorityQueue()
    current_ListNode = [(state, 'Stop', 0)]
    frontier.push(current_ListNode, 0)
    explored = set()
    ActionsList = []
    while(True):
        path_cost = 0
        if(frontier.isEmpty()):
            return []
        current_ListNode = frontier.pop()
        if(problem.isGoalState(current_ListNode[-1][0])):
            for StepInPath in current_ListNode[1:]:
                ActionsList.append(StepInPath[1])
            return ActionsList
        explored.add(current_ListNode[-1][0])
        for child in problem.getSuccessors(current_ListNode[-1][0]):
            if(child[0] not in explored):
                newListNode = current_ListNode[:]
                newListNode.append(child)
                for StepInPath in newListNode[1:]:
                    path_cost = path_cost + StepInPath[2]
                frontier.push(newListNode, path_cost)
            #else :
            #    for(ListNode in frontier):
            #        if(ListNode[-1][0] == child[0]):
                        
                # find the same child andreplace it, then calculate the new path_cost, then update()
    return None
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
