def solve(i,j,matrix,idx,n):
    if idx>=len(ip):
        return 1
    if i<0 or j<0 or i>=n or j>=n or matrix[i][j]!=ip[idx]:
        return 0
    return solve(i+1,j,matrix,idx+1,n) or solve(i,j+1,matrix,idx+1,n) or solve(i-1,j,matrix,idx+1,n) or solve(i,j-1,matrix,idx+1,n)

matrix=[['r','a','q','t'],['a','s','a','v'],['w','e','w','d'],['a','e','w','a']]
n=4
ip="saw"
f=1
for i in range(n):
    for j in range(n):
        if ip[0]==matrix[i][j]:
            if solve(i,j,matrix,0,n):
                f=0
                print("Yes")
                break
if f==1:
    print("No")
