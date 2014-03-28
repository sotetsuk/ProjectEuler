def solve():
    n = 100
    f = lambda n: (n-1)*n*(n+1)*(3*n+2)/12
    print(f(n))

if __name__ == '__main__':
    solve()
