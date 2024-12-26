## Search Problems
- Maze => Driving Directions
- 15 Sliding Tiles
## Terminology
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

![[images/Pasted image 20241226100850.png]]
### State Space
- The set of all the states reachable from the initial state by any sequence of actions.