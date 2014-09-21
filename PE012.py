from sympy import factorint

def triangular_number():
    x = 1
    ret = 0
    while True:
        ret += x
        x += 1
        yield ret

def solve():
    gen = triangular_number()
    for x in gen:
        prime_dic = factorint(x)
        num_divisor = 1
        for key, value in prime_dic.items():
            num_divisor *= value+1
        if num_divisor > 500:
            print x
            break

if __name__ == '__main__':
    solve()
