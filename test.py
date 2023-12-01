def factorial():
    stp = 1
    fact = 1
    while True:
        fact = fact * stp
        stp += 1
        yield fact


def degree(n):
    def factorization(m):
        return m**n
    return factorization


ff = factorial()
res = 1
for i in range(int(input())):
    count = degree(i)
    res += (lambda: count(1)/next(ff))()
    print(res)
