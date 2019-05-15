def bfs(t,s,g):
    front=[s]
    path=[]
    while True:
        element=front.pop(0)
        path.append(element)
        if(element==g):
            print('Goal State Found')
            print(path)
            break
        for k in t[element]:
            if front.count(k)==0 and path.count(k)==0:
                front.append(k)
        print('Frontier:', front)

def dfs(t,s,g):
    front=[s]
    path=[]
    while True:
        element=front.pop(0)
        path.append(element)
        if(element==g):
            print('Goal State Found')
            print(path)
            break
        for k in t[element]:
            front.insert(0,k)
        print('Frontier:', front)

#state_space = {'0':['5','1'], '5':['0','2','8'], '2':['5','3'], '1':['4','8','0'], '8':['1','3','5','7'], '3':['2','6','8'], '4':['1','7'], '7':['4','6','8'], '6':['3','7']}
    
State_Space={'A': ['B','C','D'], 'B' : ['E', 'F'], 'C' : ['G', 'H'], 'D': ['I','J'], 'E':['K', 'L'], 'F': ['M'], 'G' : ['N'], 'H':['O'], 'I':['P', 'Q'], 'J': ['R'], 'K':['S'], 'L':['T'], 'P':['U'], 'M': [], 'N' : [], 'Q': [], 'O':[], 'R':[], 'S':[], 'T':[],'U':[]}

bfs(State_Space, 'A', 'N') 
dfs(State_Space, 'A', 'N')

#a =[[1,2],[3,4]]
#print(a.index([1,2]))
