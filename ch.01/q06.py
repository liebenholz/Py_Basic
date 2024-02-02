def f1(values: list[int]):
    return sum(x ** 2 for x in values if x % 2 == 0)

# def f2(values: list[int]):
#    return sum(x ^ 2 for x in enumerate(values) if x % 2 == 0)

def f3(values: list[int]):
    return sum(x * x if x % 2 == 0 else 0 for x in values)

def f4(values: list[int]):
    return sum(x ^ 2 for x in values[::2])

# def f5(values: list[int]):
#    return sum(x ** 2 if x % 2 == 0 for x in values)

nlist = [1, 2, 3, 4, 8, 10, 15]

f1(nlist)
# f2(nlist)
f3(nlist)
f4(nlist)