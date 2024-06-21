
ip=[6,4,5,8,2,4]
i=0
j=len(ip)-1
max_left=ip[0]
max_right=ip[-1]
res=0
while i<j:
    if max_right>max_left:
        i+=1
        if ip[i]>max_left:
            max_left=ip[i]
        res+=max_left-ip[i]
    else:
        j-=1
        if ip[j]>max_right:
            max_right=ip[j]
        res+=max_right-ip[j]
print(res)
