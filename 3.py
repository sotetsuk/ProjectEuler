from sympy.ntheory import primefactors

def solve():
    print primefactors(600851475143)[-1]

if __name__ == '__main__':
    solve()
