
def solve(input_string,string):
    indexes = []
    for letter in input_string:
        for i in range(26):
            if letter == string[i]:
                indexes.append(i)
                break
    indexes.sort()
    res_string = ""
    for i in indexes:
        res_string+=string[i]
    return res_string

num = int(input())
strings=[]
input_strings = []
for i in range(num):
    strings.append(input())
    input_strings.append(input())
res = []
for i in range(num):
    res.append(solve(input_strings[i],strings[i]))
for string in res:
    print(string)

