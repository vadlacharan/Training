d={5:[(7,2),(3,1)],7:[(5,2),(3,2),(4,1)],3:[(5,1),(7,2),(8,2)],4:[(2,1),(7,1),(8,1)],8:[(4,1),(3,2),(2,1)],2:[(4,1),(8,1)]}
l=[]
s=5
t=2
def cost_path(s, t, path=None, cost=0):
    if path is None:
        path = []
    path.append(s)
    if s == t:
        print( "->".join(map(str, path)), cost)
    else:
        for i, w in d.get(s, []):
            if i not in path:
                cost_path(i, t, path.copy(), cost + w)
    
    path.pop()
cost_path(s,t)

