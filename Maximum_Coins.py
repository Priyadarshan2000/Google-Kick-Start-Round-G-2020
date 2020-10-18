#Priyadarshan Ghosh
import sys
from typing import List
from collections import deque


def solution(matrix: List[List[int]]) -> int:
    l = len(matrix)

    ans = - sys.maxsize
    
    starts = [[k, 0, 0] for k in range(l)] + \
             [[0, k, 0] for k in range(l)]
    q = deque(starts)

    while q:
        i, j, v = q.popleft()
        while i < l and j < l:
            v += matrix[i][j]
            i += 1
            j += 1
        ans = max(ans, v)

    return ans


if __name__ == "__main__":

    T = int(input())
    for i in range(T):
        N = int(input())
        matrix = []
        for _ in range(N):
            matrix.append(list(map(int, input().split(" "))))

        print("Case #{}: {}".format(i + 1, solution(matrix)))
