#Priyadarshan Ghosh
def solution(s: str) -> int:
    kick_stack = []
    cnt = 0

    for i, _ in enumerate(s):
        if s[i:i + 4] == "KICK":
            kick_stack.append(i)
        elif s[i: i + 5] == "START":
            cnt += len(kick_stack)

    return cnt


if __name_ == "_main_":

    N = int(input())

    for i in range(N):
        s = input()
        print("Case #{}: {}".format(i + 1, solution(s)))
