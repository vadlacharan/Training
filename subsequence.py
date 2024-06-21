s1="abcd"
s2="baababbc"
dp=[["" for i in range(len(s2))] for j in range(len(s1))]
s=""
def dfs(s1,s2,i,j):
    global s
    if i==len(s1) or j==len(s2):
        return ""
    if dp[i][j]!="":
        return dp[i][j]
    if s1[i]==s2[j]:
        dp[i][j]=s1[i]+dfs(s1,s2,i+1,j+1)
        return dp[i][j]
    else:
        lcs1=dfs(s1,s2,i+1,j)
        lcs2=dfs(s1,s2,i,j+1)
        if len(lcs1)>len(lcs2):
            dp[i][j]=lcs1
        else:
            dp[i][j]=lcs2
        return dp[i][j]
print(dfs(s1,s2,0,0))