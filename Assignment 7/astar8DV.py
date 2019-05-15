import copy
start = [[0, 5, 2], [1, 8, 3], [4, 7, 6]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

#no. of iterations of dfs depends on the sequence of children traversed

def heuristic1(arr):
    a = len(arr)
    b = len(arr[0])
    h=1
    for i in range(a):
        for j in range(b):
            if i == a-1 and j == b-1 and arr[i][j] != 0:
                h+=1
            elif arr[i][j] != 3*i + j+1:
                h+=1
    return h

#def heurisitic2(arr):
    

def getIndex(k, arr):
    for i in range(0, 3):
        for j in range(0, 3):
            if arr[i][j] == k:
                i1 = i
                j1 = j
    return i1,j1

def findChild(i,j): #to find the neighbors of any node
	child = []
	a=[i+1,j]
	b=[i-1,j]
	c=[i,j+1]
	d=[i,j-1]
	options=[a,b,c,d]
	for k in options:
		if((k[0]>=0 and k[0]<3) and (k[1]>=0 and k[1]<3)):	
			#t=(k[0]*3) + k[1] +1 
			child.append([k[0],k[1]])
	return child

def puzzle(s, g):
    frontier= [s]
    traversed = [s]
    bestChildState = []
    minh = 10
    while True:
        element = frontier.pop(0)
        if element == g:
            print('Goal found!')
            print(element)
            break

        r,c = getIndex(0, element)

        child = findChild(r,c)
        for k in child:
            a = 0
            temp = copy.deepcopy(element)
            temp[r][c] = temp[k[0]][k[1]]
            temp[k[0]][k[1]] = 0
            a = heuristic1(temp)
            if a<minh:
                minh = a
                bestChildState = temp
                print(bestChildState)
            flag = 0
            for x in range(0, len(traversed)):
                if traversed[x] == temp:
                    flag = 1
                    break
            if flag != 1:
                traversed.append(temp)
        for x in range(0, len(frontier)):
            if frontier[x] == bestChildState:
                flag = 5
        if flag != 5:
            frontier.append(bestChildState)
    return traversed

a = puzzle(start, goal)
print(len(a))