def recursion_p4(n):
    if n == 0:
        return 1
    else:
        return 2 * recursion_p4(n-1)

def recursion_p6(n):
    if n == 0:
        return 1
    else:
        return n * recursion_p6(n-1)

l = list(map(recursion_p4, range(10)))
l6 = list(map(recursion_p6, range(10)))

print(l)
print(l6)