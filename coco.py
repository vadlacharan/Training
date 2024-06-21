def solve(i,j,matrix):
    if i<0 or i > 5 or j < 0 or j > 5 or matrix[i][j] == 0:
        return 0
    else:
        matrix[i][j] = 0
    solve(i-1,j,matrix)
    solve(i+1,j,matrix)
    solve(i,j-1,matrix)
    solve(i,j+1,matrix)



n=6
matrix=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
i=4
j=6
solve(i-1,j-1,matrix)
count = 0
for row in matrix:
    for element in row:
        if element == 1:
            count +=1
print(count)