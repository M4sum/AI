import numpy as np


def change_state(a):
    loc = np.where(a == 0)
    x = [loc[0][0], loc[1][0]]
    up = [x[0], x[1]-1]
    down = [x[0], x[1]+1]
    left = [x[0]-1, x[1]]
    right = [x[0]+1, x[1]]
    moves = [up, down, left, right]
    new_states = []
    for i in moves:
        if 3 > i[0] >= 0 and 3 > i[1] >= 0:
            temp = a.copy()
            temp[i[0], i[1]], temp[x[0], x[1]] = temp[x[0], x[1]], temp[i[0], i[1]]
            new_states.append(temp)
    return new_states


def check_visited(t, e):
    for i in e:
        if np.array_equal(t, i):
            return False
    return True


def bfs(s, g):
    explored = []
    frontier = [s]
    while True:
        temp = frontier[0]
        frontier.remove(temp)
        print("Selected : ", temp, sep='\n')
        if np.array_equal(temp, g):
            print("Goal State Reached")
            break
        new_states = change_state(temp)
        for i in new_states:
            print("Added : ")
            if check_visited(i, explored):
                frontier.append(i)
                print(i)
        explored.append(temp)
        print(end='\n\n')


start = np.array([[0, 5, 2], [1, 8, 3], [4, 7, 6]])
goal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
bfs(start, goal)
