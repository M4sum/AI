import copy
start = [['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '-', '-', '-', '-', '-', '-', '#'],
        ['#', '-', '#', '#', '#', '-', '-', '#'],
        ['#', '-', '#', '*', '#', '-', '-', '#'],
        ['#', '-', '-', '-', '#', '-', '-', '#'],
        ['#', '-', '#', '#', '#', '-', '-', '#'],
        ['#', 'P', '-', '-', '-', '-', '-', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#']]
goal = [['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '-', '-', '-', '-', '-', '-', '#'],
        ['#', '-', '#', '#', '#', '-', '-', '#'],
        ['#', '-', '#', 'P', '#', '-', '-', '#'],
        ['#', '-', '-', '-', '#', '-', '-', '#'],
        ['#', '-', '#', '#', '#', '-', '-', '#'],
        ['#', '-', '-', '-', '-', '-', '-', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#']]

def getIndex(k, arr):
    for i in range(0, len(arr)):
            for j in range(0, len(arr[0])):
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
    options=[a,c,b,d]
    for k in options:
        if((k[0]>=0 and k[0]<len(arr)) and (k[1]>=0 and len(arr[0]))):
            if arr[k[0]][k[1]] == '*':
                child.clear()
                child.append([k[0],k[1]])
                break
            if arr[k[0]][k[1]] != '#':
                child.append([k[0],k[1]])
    return child

def bfs(s, g):
    frontier= [s] 
    traversed = [s]
    while True:
        element = frontier.pop(0)
        if element == g:
            print('Goal found!')
            print(element)
            break

        r,c = getIndex('P', element)

        child = findChild(element,r,c)
        for k in child:
            temp = copy.deepcopy(element)
            if temp[k[0]][k[1]] == '*':
                temp[r][c] = '-'
                temp[k[0]][k[1]] = 'P'
            else:
                temp[r][c] = temp[k[0]][k[1]]
                temp[k[0]][k[1]] = 'P'
            flag = 0
            for x in range(0, len(traversed)):
                if traversed[x] == temp:
                    flag = 1
                    break
            if flag != 1:
                frontier.insert(0,temp)
                traversed.append(temp)
    return traversed

a = bfs(start, goal)
print(len(a))