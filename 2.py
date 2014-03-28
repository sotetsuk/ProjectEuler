def fib():
    x, y = 1, 2
    while True:
        yield x
        x, y = y, x+y

def solve():
    gen = fib()
    ans = 0
    for x in gen:
        if x > 4000000:
            break
        if x % 2 == 0:
            ans += x
    print ans

if __name__ == '__main__':
    solve()
