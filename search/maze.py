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
        # Initially the frontier is represented by an empty list.
        self.frontier = []

    # Adds a new node to the frontier by appending the node at the end of the list.
    def add(self, node):
        self.frontier.append(node)

    # Checks if the frontier contains a particlart state.
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    # Checks if the frontier is empty.
    def empty(self):
        return len(self.frontier) == 0

    # Function to remove something from the frontier.
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            # Take the last node from the frontier to remove, since we are following the stack data structure.
            node = self.frontier[-1]
            # Remove the last added node from the list of frontier.
            self.frontier = self.frontier[:-1]
            # Return the node.
            return node

# This class inherits all the functionalities fro the StackFrontier, except the functions that are overwritten in this class.
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

# This class handels the process of taking a Maze like text file and figuring out how to solve it.
class Maze():
    # Read the file, make sure the required states are present, check height and width of the maze, check the coordinates of start and end position, mark the coordinates with walls.
    def __init__(self, filename):

        # Read the file
        with open(filename) as f:
            contents = f.read()

        # Validate that both start and goal state is present.
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        # Split each line of content into an array of lines.
        contents = contents.splitlines()
        # Get the height of the maze.
        self.height = len(contents)
        # Get the width of the maze.
        self.width = max(len(line) for line in contents)

        self.walls = []

        # Define the start, end and wall position.
        for i in range(self.height):
            row = []

            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)

            self.walls.append(row)

        self.solution = None

    # Print the solution.
    def print(self):

        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    # Check out all the movable neighbour positions and return the list.
    def neighbors(self, state):
        # Get the coordinates of the current state.
        row, col = state

        # Define the candidate, that the current state can take to change the state.
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []

        # Loop through all the possible candidates.
        for action, (r, c) in candidates:
            # Make sure the row and column's coordinates does not exceeds the maze or there is no wall at the given coordinates.
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                # Add all the possible candidates into the result list.
                result.append((action, (r, c)))

        # Return result.
        return result


    def solve(self):

        # Number of states explored.
        self.num_explored = 0

        # Initialize frontier to the starting position.
        start = Node(state=self.start, parent=None, action=None)
        
        # Initialize a new frontier and add the starting position.
        frontier = StackFrontier()
        frontier.add(start)

        # Initialize an empty explored set.
        self.explored = set()

        # Keep looping untill the current start becomes a goal state.
        while True:

            # Make sure that the frontier is not empty.
            if frontier.empty():
                raise Exception("No Solution")

            # Remove a node from the frontier.
            node = frontier.remove()

            # Increase the number of state explored.
            self.num_explored += 1

            # Check if the current state is the goal state.
            if node.state == self.goal:
                actions = []
                cells = []

                # Loop through all the parents of the current node to check the path taken from the initial state to the goal state.
                while node.parent is not None:
                    # Append all the actions taken in the actions list.
                    actions.append(node.action)
                    # Append all the coordinates moved taken in the cells list.
                    cells.append(node.state)
                    # Change the value of the node to the parent of the current node.
                    node = node.parent

                # Reverse the actions and coordinates moved to get them from initial state to the goal state.
                actions.reverse()
                cells.reverse()

                # Update the solution.
                self.solution = (actions, cells)
                
                return

            # Add the current state in the list of explored states. 
            self.explored.add(node.state)

            # Loop through the list of all the possible neighbours of the current state.
            for action, state in self.neighbors(node.state):
                # Make sure that the possible neighbours are not already in the frontier's list or are not explored.
                if not frontier.contains_state(state) and state not in self.explored:
                    # Create a new node for the neighbour and append it into the frontier.
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

    # Generate the output image of the solution.
    def output_image(self, filename, show_solution=True, show_explored=False):
        from PIL import Image, ImageDraw
        cell_size = 50
        cell_border = 2

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                # Walls
                if col:
                    fill = (40, 40, 40)

                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)

                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)

                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)

                # Empty cell
                else:
                    fill = (237, 240, 252)

                # Draw cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        img.save(filename)


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python maze.py maze.txt")

    # Create a new Maze object.
    m = Maze(sys.argv[1])
    print("Maze:")
    m.print()
    print("Solving...")
    m.solve()
    print("States Explored:", m.num_explored)
    print("Solution:")
    m.print()
    m.output_image("maze.png", show_explored=True)


if __name__ == "__main__":
    main()