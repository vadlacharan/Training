

ip=[1,3,4,5]
cost=17
dp=[[-1 for i in range(cost+1)] for j in range(len(ip))]
for i in range(cost+1):
    dp[0][i]=i
print(dp)
for i in range(1,len(ip)):
    for j in range(cost+1):
        if j<ip[i]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=min(1+dp[i][j-ip[i]],dp[i-1][j])
print(dp)