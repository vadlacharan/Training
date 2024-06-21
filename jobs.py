l=[[1,2],[2,5],[5,6],[6,7],[7,8],[8,9]]
p=[5,6,6,4,11,2]
max1=0
for i in range(len(l)):
    maxx=p[i]
    c=l[i][1]
    for j in range(len(l)-1):
        if c<=l[j+1][0]:
            maxx=maxx+p[j+1]
            c=l[j+1][1]
    max1=max(maxx,max1)
print(max1)