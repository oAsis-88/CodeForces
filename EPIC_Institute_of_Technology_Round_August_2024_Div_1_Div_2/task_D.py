from collections import deque

def breadth_first_search(graph, start):
  # Initialize the queue with the start node
  queue = deque([start])

  # Keep track of visited nodes
  visited = set()

  # Loop until the queue is empty
  while queue:
    # Get the next node from the queue
    node = queue.popleft()

    # Skip the node if it has already been visited
    if node in visited:
      continue

    # Visit the node
    print(node)
    visited.add(node)

    # Add the neighbors of the node to the queue
    for neighbor in graph[node]:
        print(neighbor, end=" ")
        queue.append(neighbor)
    print()

# Create an adjacency matrix representing a graph
graph = [[0, 1, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 1, 1],
         [0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0]]

# Start the breadth-first search at node 0
breadth_first_search(graph, 0)