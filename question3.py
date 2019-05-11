import numpy as np


def change_state(a):
    loc = np.where(a == 'P')
    x = [loc[0][0], loc[1][0]]
    up = [x[0], x[1]-1]
    down = [x[0], x[1]+1]
    left = [x[0]-1, x[1]]
    right = [x[0]+1, x[1]]
    moves = [up, down, left, right]
    new_states = []
    for i in moves:
        if 8 > i[0] >= 0 and 8 > i[1] >= 0 and a[i[0], i[1]] != '#':
            temp = a.copy()
            temp[i[0], i[1]], temp[x[0], x[1]] = temp[x[0], x[1]], temp[i[0], i[1]]
            if temp[x[0], x[1]] == '*':
                temp[x[0], x[1]] = '-'
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
        print("Move Done : ")
        pos = np.where(temp == 'P')
        print((pos[0][0]+1, pos[1][0]+1), end=', ')
        print(end='\b\b\n')
        if np.array_equal(temp, g):
            print("Goal State Reached")
            break
        new_states = change_state(temp)
        print("Next Possible Moves: ")
        for i in new_states:
            if check_visited(i, explored):
                frontier.append(i)
                pos = np.where(i == 'P')
                print((pos[0][0]+1, pos[1][0]+1), end=', ')
        explored.append(temp)
        print(end='\b\b\n\n')


start = np.array([['#', '#', '#', '#', '#', '#', '#', '#'],
                          ['#', '-', '-', '-', '-', '-', '-', '#'],
                          ['#', '-', '#', '#', '#', '-', '-', '#'],
                          ['#', '-', '#', '*', '#', '-', '-', '#'],
                          ['#', '-', '-', '-', '#', '-', '-', '#'],
                          ['#', '-', '#', '#', '#', '-', '-', '#'],
                          ['#', 'P', '-', '-', '-', '-', '-', '#'],
                          ['#', '#', '#', '#', '#', '#', '#', '#']])
goal = np.array([['#', '#', '#', '#', '#', '#', '#', '#'],
                          ['#', '-', '-', '-', '-', '-', '-', '#'],
                          ['#', '-', '#', '#', '#', '-', '-', '#'],
                          ['#', '-', '#', 'P', '#', '-', '-', '#'],
                          ['#', '-', '-', '-', '#', '-', '-', '#'],
                          ['#', '-', '#', '#', '#', '-', '-', '#'],
                          ['#', '-', '-', '-', '-', '-', '-', '#'],
                          ['#', '#', '#', '#', '#', '#', '#', '#']])
bfs(start, goal)

