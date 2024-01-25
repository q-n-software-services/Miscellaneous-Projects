import itertools
import sys

NO_PATH = 999999999999

graph = [[0, 7, NO_PATH, 8],

         [2, 0, NO_PATH, 4],

         [NO_PATH, 1, 0, NO_PATH],

         [NO_PATH, NO_PATH, 2, 0]]

MAX_LENGTH = len(graph[0])

print(graph[0])
print(graph[1])
print(graph[2])
print(graph[3])
print()



def floyd(distance):
    for intermediate in range(MAX_LENGTH):
        for start_node in range(MAX_LENGTH):
            for end_node in range(MAX_LENGTH):
                # Assume that if start_node and end_node are the same
                # then the distance would be zero
                if end_node == start_node:
                    distance[start_node][end_node] = 0
                    continue
                # return all possible paths and find the minimum
                distance[start_node][end_node] = min(distance[start_node][end_node], distance[start_node][intermediate] + distance[intermediate][end_node])

                # Any value that have sys.maxsize has no path

    print(distance[0])
    print(distance[1])
    print(distance[2])
    print(distance[3])



floyd(graph)

