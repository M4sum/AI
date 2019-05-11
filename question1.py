def bfs(t, s, g):
    frontier = [s]
    while True:
        temp = frontier.pop(0)
        print("Current State :", temp, end=' ')
        if temp == g:
            print("Goal State Found")
            break
        for k in t[temp]:
            frontier.append(k)
        print("Frontier :", frontier)


def dfs(t, s, g):
    frontier = [s]
    while True:
        temp = frontier.pop(0)
        print("Current State :", temp, end=' ')
        if temp == g:
            print("Goal State Found")
            break
        for k in t[temp]:
            frontier.insert(t[temp].index(k), k)
        print("Frontier :", frontier)


State_Space = {'A': ['B', 'C', 'D'], 'B': ['E', 'F'], 'C': ['G', 'H'], 'D': ['I', 'J'], 'E': ['K', 'L'], 'F': ['M'], 'G': ['N'], 'H': ['O'], 'I': ['P', 'Q'], 'J': ['R'], 'K': ['S'], 'L': ['T'], 'M': [], 'N': [], 'O': [], 'P': ['U'], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': []}
# non = int(input("Enter the number of nodes in state space : "))
# print("START ENTERING THE NODES OF THE STATE SPACE ")
# for i in range(non):
#     name = input("Enter the name of the node : ")
#     children = input("Enter the Children of the Node {} : ".format(name)).split()    #     State_Space[name] = children
# print(State_Space)
bfs(State_Space, 'A', 'H')
dfs(State_Space, 'A', 'H')
