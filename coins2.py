def solve():
    dp=[[0 for i in range(n+1)]for j in range(len(s))]
    for i in range(n+1):
        if i==0 or i==s[0]:
            dp[0][i]=1
    for i in range(1,len(s)):
        for j in range(n+1):
            if j==0:
                dp[i][j]=1
            elif j<s[i]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j-s[i]]
    print(dp)
    if dp[-1][-1]:
        print("Yes")
    else:
        print("No")
solve() 