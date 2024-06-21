l = [3,2,5,4,1,6,8]
res = []
def solve(idx,l,out):
    global res
    if idx>=len(l):
        return 
    if len(out) == 3:
        res.append(out[:])
        return
    solve(idx+1,l,out+[l[idx]])
    solve(idx+1,l,out)
solve(0,l,[])
print(res)
