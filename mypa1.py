from __future__ import annotations
from collections import deque
import copy

from mypa0_sol import Graph, is_in

class Problem:
    """ Problem class
    """
    def __init__(self, graph: Graph, init_node: int, goals: list[int]) -> None:
        """initialization

        Args:
            graph (Graph): a graph (use Graph class from pa0)
            init_node (int): an initial state (id)
            goals (list[int]): a list of goal states (id)
        """
        pass
    
    def check_goal(self, node_id: int) -> bool:
        """check if a given state (id) is a goal

        Args:
            node_id (int): a node id

        Returns:
            bool: True if goal; else False
        """
        pass

class TreeNode:
    """TreeNode class to store a search tree 
    Note: this is a separate tree from the original graph to store the search process
    """
    def __init__(self, node_id: int, parent: int=None, path_cost: float=0.0):
        """Initialization
        Each instance should be the following member variables:
        - id (int): node id in the original graph
        - parent (int): a parent node id in the search tree
        - path_cost (float): the total path cost from the initial state to this node on the search tree
        - depth (int): the depth of this node in the search tree. an initial state's depth is 0.

        Args:
            node_id (int)
            parent (int, optional)
            path_cost (float, optional): Defaults to 0.0.
        """
        pass
    
    def __repr__(self) -> str:
        """Show the node id

        Returns:
            str: node id
        """
        pass
    
    def __lt__(self, node: TreeNode):
        """less than relation between self and a given node.
        n_i < n_j when i < j where i and j are ids
        """
        pass
    
    def path(self) -> list[int]:
        """A path from the initial node to this node on the search tree

        Returns:
            list[int]: a list of node ids representing the path [initial node id, ..., this node's id]
        """
        pass

class SearchAgent:
    """Search Agent class
    This will be a base class for other search agents
    """
    def __init__(self, name: str) -> None:
        """Initialization
        Each instance should be the following member variables:
        - search_name (str): a search name
        - expanded_nodes (list[int]): a list of expanded nodes (ids)
        - front (list[TreeNode]): a list of frontier nodes (TreeNodes)
        - front_history (list[dequeue[TreeNode]]): [grading purpose only] a list of frontiers. record the frontier when it's updated.

        Args:
            name (str): a search name
        """
        pass

    def tiebreaker(self,l: list[int]) -> list[int]:
        """a tie-breaking rule among the nodes in the same level: Use the increasing order 1 -> 2 -> ....

        Args:
            l (list[int]): a list of node ids

        Returns:
            list[int]: a list of node ids
        """
        pass

    def count_visited_nodes(self) -> int:
        """return the total number of nodes that were wither expanded or put into the frontier.

        Returns:
            int: the total number of nodes expanded or in the frontier
        """
        pass
    
    def count_expanded_nodes(self) -> int:
        """Count the number of nodes in the expanded node set

        Returns:
            int: the number of nodes in the expanded node set
        """
        pass
    
    def calc_avg_front_size(self) -> float:
        """Calculate the average frontier size based on the frontier history.

        Returns:
            float: the average frontier size
        """
        pass

class BFSAgent(SearchAgent):
    """BFS class
    """
    def bfs(self, problem: Problem) -> 'TreeNode':
        """BFS algorithm

        Args:
            problem (Problem): a problem

        Returns:
            TreeNode: a goal TreeNode (None if no goal is attainable.)
        """
        pass

class DFSAgent(SearchAgent):
    """DFS class
    """
    def dfs(self, problem):
        """DFS algorithm

        Args:
            problem (Problem): a problem

        Returns:
            TreeNode: a goal TreeNode (None if no goal is attainable.)
        """        
        pass

    def tiebreaker(self, l: list[int]) -> list[int]:
        """overwrite the tiebreaker function for DFS (if needed). Use the increasing order: 1 -> 2 -> ....

        Args:
            l (list[int]): a list of node ids

        Returns:
            list[int]: a list of node ids
        """
        pass
        
class IterativeDeepeningSearchAgent(SearchAgent):
    """Iterative Deepening Search class
    """
    def ids(self, problem: Problem, max_depth: int=1000) -> TreeNode:
        """Iterative deepening search algorithm. Use the dls function to implement ids.

        Args:
            problem (Problem): a problem
            max_depth (int, optional): max search depth. Defaults to 1000.

        Returns:
            TreeNode: a goal TreeNode (None if no goal is attainable.)
        """
        pass

    def dls(self, problem: Problem, limit: int) -> TreeNode:
        """Depth limited search algorithm.
        Hint: You may want to define an inner function and recursively call it.

        Args:
            problem (Problem): a problem
            list (int, optional): search depth limit

        Returns:
            TreeNode: a goal TreeNode (None if no goal is attainable.)
        """
        pass