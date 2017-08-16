# -*- coding: cp949 -*-
# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""
# -*- coding: cp949 -*-

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def iterativeDeepingSearch(problem):
    "*** YOUR CODE HERE ***"

    num = 0 # num = depth �Ǻ�
    while 1:
        fringe = util.Stack() # fringe�� ���� ����(��������)�� �� node, action, cost ������ �޽��ϴ�.
        fringe.push((problem.getStartState(), [], 0))
        visited = [] # �湮�� ������� �Ǻ�
        
        while not fringe.isEmpty(): # fringe�� ������� ������(�� �̻� �� ��� ����������)
           node, actions, cost = fringe.pop()
           if problem.isGoalState(node): #��尡 goal�̸� �迭�� �ִ� action�� ���� �̵�
                return actions

           visited.append(node) # �湮�� ��� �߰�
         
           if cost < num: # �� ���������� �� ��� �̵��� ������ cost�� �� 1�� �þ�� ������ cost�� ����� depth ������ �Ͽ� �� ��° depth���� �Ǻ���
            for state, action, costs in problem.getSuccessors(node): #��� extend��
               if not state in visited:  #�湮���� ���� ����̸�
                 fringe.push((state, actions + [action], cost + costs)) #fringe�� �� state, action, cost �߰�
                
        num = num + 1  # �� iterative ���� depth �Ǻ��� �þ   
                   
    # node =  �̵��� state, action = �̵�, cost = �̵��� �Ÿ�
               


def Heuristic(state, problem=None):
    "*** YOUR CODE HERE ***"
    return 22

def aStarSearch(problem, heuristic=nullHeuristic):
    

    fringe = util.PriorityQueue() # �켱����ť ������ �� ����� cost + heuristic���� �켱������ ������ �ٸ�
    start = problem.getStartState()
    fringe.push((start, [], 0), heuristic(start, problem))
    expanded = [] # expand�� ��忴���� �Ǻ�
    
    while not fringe.isEmpty(): #fringe�� ������� ������(�� �̻� �� ��� ���� ������)
        node, actions, cost = fringe.pop()

        if problem.isGoalState(node): #��尡 goal�̸� �迭�� �ִ� action�� ���� �̵�
            return actions

        expanded.append(node) # expand�� ��� �߰�
        
        for state, action, costs in problem.getSuccessors(node): #��� expand
            new_actions = actions + [action] # �� action �߰�
            new_cost = cost + costs # �̵� �Ÿ� ����
            total = new_cost + heuristic(state, problem) # ���� �̵��� �Ÿ� + heuristic
            if not state in expanded: # expand�� ��� �ƴϸ� fringe �߰�
                fringe.push((state, new_actions, new_cost), total)
                
        # node =  �̵��� state, action = �̵�, cost = �̵��� �Ÿ�

# Abbreviations
ids= iterativeDeepingSearch
astar = aStarSearch
