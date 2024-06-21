num = int(input())

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
left = 1
right = num-1
flag1 = 1
flag2 = 1
while(left<=right):
    flag1 = is_prime(left)
    flag2 = is_prime(right)
    if flag1 == 1 and flag2 == 1:
        print(left,right,"True")
        break
    left+=1
    right-=1
else:
    print("False")

            
