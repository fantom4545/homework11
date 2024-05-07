def test(*params):
    print(*params)
    print(params)


test(1, 2, 2, 2)


def sum(n):
    if n == 0:
       return 1
    else:
        return n * sum(n - 1)
print(sum(7))

