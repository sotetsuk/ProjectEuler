import numpy as np
import sys

N = 1000000
arr = np.zeros(100000000000, dtype=np.int64)
arr[1] = 1

def dfs(n):
    if arr[n] != 0:
        return arr[n]
    else:
        arr[n] = dfs(3 * n + 1) + 1 if n % 2 == 1 else dfs(n / 2) + 1
        return arr[n]

def solve():
    M = 0
    ans = 0
    for i in range(1, N):
        if dfs(i) > M:
            M = arr[i]
            ans = i

    print ans

if __name__ == '__main__':
    solve()
