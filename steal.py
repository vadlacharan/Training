l=[13,9,4,10,5,7]
def solve(idx,l):
    if idx>=len(l):
        return 0
    return max(l[idx]+solve(idx+2,l),solve(idx+1,l))
print(solve(0,l))
