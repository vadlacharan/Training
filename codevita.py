string="school"
num = 3
operations= ["L2","R3","L1"]
res = ""
for operation in operations:
    res+=string[int(operation[1])]

left,right = 0,2
string_length = len(string)
combinations = []
while( right < string_length):
    combinations.append(string[left:right+1])
    right+=1
    left+=1

flag = 0
for combination in combinations:
    sorted_combination = sorted(combination)
    res_sorted = sorted(res)
    if sorted_combination == res_sorted:
        flag = 1

if flag == 1:
    print("yes")
else:
    print("no")
