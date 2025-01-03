## Search Problems
- Maze => Driving Directions
- 15 Sliding Tiles
---
## Terminologies
### Agent
- An entity that perceives its environment and acts upon that environment.
### State
- A configuration of the agent and its environment.
- For eg, in a 15 sliding tile example, the initial position of the tiles can be the state.
### Initial State
- The state from where the agent begins.
### Actions
- Choices that can be made in a state.
- Actions(s) returns the set of actions that can be executed in a state s.
	- "Actions(s)" is a function which takes 's' parameter which can be the initial state of a problem.
	- It returns as output the set of actions that can be executed.
### Transition Model
- A description of what state results from performing any applicable action in any state.
- Result(s, a) returns the state resulting from performing action a in state s.

![transition model](./images/Pasted%20image%2020241226100850.png)
### State Space
- The set of all the states reachable from the initial state by any sequence of actions.

![state space](./images/Pasted%20image%2020241227113412.png)

**Simplified Representation as graph**

![image](./images/Pasted%20image%2020241227113502.png)
### Goal Test
- A way to determine whether a given state is a goal state.
### Path Cost
- Numerical cost associated with a given path.

![path cost](./images/Pasted%20image%2020241227114014.png)
### Solution
- A sequence of actions that leads from the initial state to a goal state.
### Optimal Solution
- A solution that has the lowest path cost among all solutions.
---
Now we need to begin to figure out that how is it that we are going to solve this kind of search problem. To do that our computer needs to represent a whole bunch of data about the problem. Often times when we are packaging the whole bunch of data, related to a state, together, we will do so using a data structure, that we are going to call a Node.
## Node
- A data structure that keeps track of
	- A state
	- A parent (node that generated this node)
	- An action (action applied to parent to get current node)
	- A path cost (from initial state to current node)
From a given state, we have multiple options to take. We are going to explore those options. Once we explore those options, we will find that more options than that are going to make themselves available. We are going to consider all of the available options to be stored inside a single data structure that we will call the frontier.
## Approach
- State with a frontier that contains the initial state.
- Repeat
	- If frontier is empty, then there is no solution.
	- Remove a node from the frontier.
	- If the node contains the goal state, return the solution.
	- Expand node, adding resulting nodes to the frontier.

**Example**

1. Find a path from A to E.

![image](./images/Pasted%20image%2020250101123136.png)

Frontier = A  
Step 1: Remove the node from frontier  
Step 2: A is not the goal state.  
Step 3: Expand node, adding resulting nodes to the frontier, that is, Frontier = B.  

Frontier = B  
Step 1: Remove the node from frontier  
Step 2: B is not the goal state.  
Step 3: Expand node, adding resulting nodes to the frontier, that is, Frontier = C, D.  

Frontier = C, D
Step 1: Remove the node C from the frontier.  
Step 2: C is not the goal state.  
Step 3: Expand node, adding resulting nodes to the frontier, that is, Frontier = E, D.  

Frontier = E, D  
Step 1: Remove the node E from the frontier.  
Step 2: E is the goal state. Hence, return the solution.  

2. Find a path from A to E.

![image](./images/Pasted%20image%2020250101123915.png)

Frontier = A  
Step 1: Remove the node from frontier  
Step 2: A is not the goal state.  
Step 3: Expand node, adding resulting nodes to the frontier, that is, Frontier = B.  

Frontier = B  
Step 1: Remove the node from frontier  
Step 2: B is not the goal state.  
Step 3: Expand node, adding resulting nodes to the frontier, that is, Frontier = A, C, D.  

Frontier = A, C, D  
Step 1: Remove the node A from the frontier.  
Step 2: A is not the goal state.  
Step 3: Expand node, adding resulting nodes to the frontier, that is, Frontier = B, C, D.  

Frontier = B, C, D  
Step 1: Remove the node from frontier  
Step 2: B is not the goal state.  
Step 3: Expand node, adding resulting nodes to the frontier, that is, Frontier = A, C, D.  

This can get into an infinite loop since it keeps going back and frontend between the two states. The solution to this problem is to keep track of already visited node. Once the state is explored, dont bother to add it back to the frontier.

## Revised Approach
- Start with a frontier that contains the initial state.
- Start with an empty explored set.
- Repeat:
	- If the frontier is empty, there is no solution.
	- Remove a node from the frontier.
	- If the node contains the goal state, return the solution.
	- Add the node to the explored state.
	- Expand node, adding the resulting node to the frontier, if that node is not already in the frontier or explored yet.
The frontier is a data structure. The order in which we remove the node will be that of a stack, that is, last in first out.

**Example**

1. Find a path from A to E.

![image](./images/Pasted%20image%2020250103090318.png)

Frontier = A  
Step 1: Remove the node from frontier.  
Step 2: A is not the goal state.  
Step 3: Add A in the Explored Set, that is, Explored Set = A.  
Step 4: Expand node, adding resulting nodes to the frontier, that is, Frontier = B.  

Frontier = B  
Step 1: Remove the node from frontier  
Step 2: B is not the goal state.  
Step 3: Add B in the Explored Set, that is, Explored Set = A, B.  
Step 4: Expand node, adding resulting nodes to the frontier, that is, Frontier = C, D.  

Frontier = C, D  
Step 1: Remove the node D from the frontier. // Removing D and not C because we are following stack approach, that is, last in first out.  
Step 2: D is not the goal state.  
Step 3: Add D in the Explored Set, that is, Explored Set = A, B, D.  
Step 3: Expand node, adding resulting nodes to the frontier, that is, Frontier = C, F.  

Frontier = C, F  
Step 1: Remove the node F from the frontier.  
Step 2: F is not the goal state.  
Step 3: Add F in the Explored Set, that is, Explored Set = A, B, D, F.  
Step 3: Expand node, adding resulting nodes to the frontier, that is, Frontier = C.  

Frontier = C  
Step 1: Remove the node C from the frontier.  
Step 2: C is not the goal state.  
Step 3: Add C in the Explored Set, that is, Explored Set = A, B, D, F, C.  
Step 3: Expand node, adding resulting nodes to the frontier, that is, Frontier = E.  

Frontier = E  
Step 1: Remove the node E from the frontier.  
Step 2: E is the goal state. Hence, return the solution.  

When we use Stack approach, when watching visually, we first go deep on one side and then explore the other side. We first go from A -> B -> D -> F -> C -> E. This type of search is called as Depth-First Search.
## Depth-First Search (DFS)
- Search algorithm that always expands the deepest node in the frontier.
- We use Stack data structure for the depth first search. It follows last in first out approach.
## Breadth-First Search (BFS)
- Search algorithm that always expands the shallowest node in the frontier.
- We use Queue data structure for the depth first search. It follows first in first out approach.

**Example**

1. Find a path from A to E.

![image](./images/Pasted%20image%2020250103090318.png)

Frontier = A  
Step 1: Remove the node from frontier.  
Step 2: A is not the goal state.  
Step 3: Add A in the Explored Set, that is, Explored Set = A.  
Step 4: Expand node, adding resulting nodes to the frontier, that is, Frontier = B.  

Frontier = B  
Step 1: Remove the node from frontier  
Step 2: B is not the goal state.  
Step 3: Add B in the Explored Set, that is, Explored Set = A, B.  
Step 4: Expand node, adding resulting nodes to the frontier, that is, Frontier = C, D.  

Frontier = C, D  
Step 1: Remove the node C from the frontier. // Removing C and not D because we are following queue approach, that is, first in first out.  
Step 2: C is not the goal state.  
Step 3: Add C in the Explored Set, that is, Explored Set = A, B, C.  
Step 3: Expand node, adding resulting nodes to the frontier, that is, Frontier = D, E.  

Frontier = D, E  
Step 1: Remove the node D from the frontier.  
Step 2: D is not the goal state.  
Step 3: Add D in the Explored Set, that is, Explored Set = A, B, C, D.  
Step 3: Expand node, adding resulting nodes to the frontier, that is, Frontier = E, F.  

Frontier = E, F  
Step 1: Remove the node E from the frontier.  
Step 2: E is the goal state. Hence, return the solution.  

---
## Maze Problem
### Depth-First Search

![image](./images/Pasted%20image%2020250103092351.png)

- As long as our maze is finite, DFS is going to find a solution.
- DFS does not necessarily will be the optimal solution. For example, in the following maze, there are multiple solutions. If it chooses the right direction in the first turn, it reaches the goal faster; however, there is not a particular reason for the DFS to choose that first. Alternatively, DFS can choose the other path and make the solution much longer.

 ![image](./images/Pasted%20image%2020250103092930.png)
### Breadth-First Search
- BFS takes the approach of exploring all the possible paths at the same time. It takes on step on all the sides.

![image](./images/Pasted%20image%2020250103093350.png)

- Although in this case, we need to explore some paths that does not takes us anywhere, the path that we found to the goal, was the optimal path, that is, the shortest way, we can get to the goal.
- When looking at the bigger maze, although the BFS finds the optimal solution, the trade off is that, it needs to explore a lot of state before reaching the goal.

![image](./images/Pasted%20image%2020250103093712.png)
