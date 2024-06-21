ip = "the quick brown fox jumps over the lazy dog"

"""if len(set(ip)) != 27:
    print("False")
else:
    print("True")"""


my_dict = dict()

for letter in ip:
    if ord(letter) >= 97 and ord(letter) <= 122:
        if letter not in my_dict:
            my_dict[letter] = 1
print(len(my_dict))
if len(my_dict) == 26:
    print("Yes")
else:
    print("No")
