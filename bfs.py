"""graph={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
def bfs(start,graph,visited):
    queue=[start]
    out=[start]
    visited.add(start)
    while queue:
        node=queue.pop(0)
        for i in graph[node]:
            if i not in out:
                queue.append(i)
                out.append(i)
                visited.add(i)
    print(out)
bfs(5,graph,set())"""

d1={5:[(7),(3)],
   7:[(5),(4),(3)],
   4:[(7),(8),(2)],
   3:[(5),(7),(8)],
   8:[(3),(4),(2)],
   2:[(4),(8)]}


def bfs_spanning_tree(x):
    v=[]
    q=[x]
    while q:
        for i in d1[q[0]]:
            if i not in q and i not in v:
                q.append(i)
        v.append(q.pop(0))
        print(v[-1],end=" ")



bfs_spanning_tree(5)