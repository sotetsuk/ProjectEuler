from sympy.ntheory.generate import primerange

def solve():
    ans = 0
    for i in primerange(1, 2000000):
        ans += i
    print(ans)

if __name__ == '__main__':
    solve()
