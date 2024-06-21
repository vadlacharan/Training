n = int(input())
arr=[]
for  i in range(n):
    arr.append(int(input()))

arr_sum = sum(arr)

print( (n * ( n+1))//2 - arr_sum )  