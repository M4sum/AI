import copy
start = [[0, 5, 2], [1, 8, 3], [4, 7, 6]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

#no. of iterations of dfs depends on the sequence of children traversed

def getIndex(k, arr):
    for i in range(0, 3):
            for j in range(0, 3):
                if arr[i][j] == k:
                    i1 = i
                    j1 = j
    return i1,j1

def findChild(arr,i,j): #to find the neighbors of any node
    child = []
    a=[i+1,j]
    b=[i-1,j]
    c=[i,j+1]
    d=[i,j-1]
    options=[a,b,c,d]
    for k in options:
        if((k[0]>=0 and k[0]<3) and (k[1]>=0 and k[1]<3)):	
            if arr[k[0]][k[1]] == 0:
                    child.clear()
                    child.append([k[0],k[1]])
                    break
            child.append([k[0],k[1]])
    return child

def bfs(s, g):
    frontier= [s] 
    traversed = [s]
    while True:
        element = frontier.pop(0)
        print(element)
        if element == g:
            print('Goal found!')
            print(element)
            break

        r,c = getIndex(0, element)

        child = findChild(element,r,c)
        for k in child:
            temp = copy.deepcopy(element)
            temp[r][c] = temp[k[0]][k[1]]
            temp[k[0]][k[1]] = 0
            flag = 0
            for x in range(0, len(traversed)):
                if traversed[x] == temp:
                    flag = 1
                    break
            if flag != 1:
                frontier.append(temp)
                traversed.append(temp)
    return traversed

a = bfs(start, goal)
print(len(a))