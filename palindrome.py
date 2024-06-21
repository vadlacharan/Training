def next_palindrome(n):
    s = str(n)
    length = len(s)
    
    
    half_len = (length + 1) // 2
    left_half = s[:half_len]
    
    if length % 2 == 0:
        palindrome = left_half + left_half[::-1]
    else:
        palindrome = left_half + left_half[-2::-1]
    
    if int(palindrome) > n:
        return int(palindrome)
    
    left_half = str(int(left_half) + 1)

    if length % 2 == 0:
        palindrome = left_half + left_half[::-1]
    else:
        palindrome = left_half + left_half[-2::-1]
    
    return int(palindrome)

number = 76583
print(next_palindrome(number))  