def isPalindromic(num):
    num = str(num)
    return num == num[::-1]

def solve():
    ans = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i * j
            if isPalindromic(num):
                ans = max(ans, num)
    print ans

if __name__ == '__main__':
    solve()
