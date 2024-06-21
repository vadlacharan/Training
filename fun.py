def fun(a, b, index):
    global res
    while a and a[0] % 2 != 0:
        a.pop(0)
    if not a or index >= len(b):
        return
    if (a[0] + b[index]) % 2 != 0:
        res.append(a[0] + b[index])
    fun(a, b, index + 1)

a = [6, 3, 2, 9, 4, 7]
b = [8, 7, 5, 3, 6, 9]
res = []
fun(a, b, 0)
print(res)
