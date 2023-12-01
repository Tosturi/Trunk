def factorial():
    stp = 1
    fact = 1
    while True:
        fact = fact * stp
        stp += 1
        yield fact
        # if stp > steps:
        #     return


def iks():
    step = 1
    while True:
        step += 1
        yield step


ff = factorial()
res = 1
for _ in range(10):
    f = (lambda x, y: (1**x/y))(iks().__next__(), factorial().__next__())
    res += f
    print(res)