graph={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
res = []


def dfs(start,visited,graph,end,cnt):
    global res
    visited.add(start)
    res.append(start)
    for i in graph[start]:
        if i not in visited:
            dfs(i,visited,graph,end,cnt+1)

dfs(5,set(),graph,2,0)
print(res)