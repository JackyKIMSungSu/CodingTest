import sys
from itertools import combinations


def count_diff(MBTI1, MBTI2):
    return sum(c1 != c2 for c1, c2 in zip(MBTI1, MBTI2))

num = int(sys.stdin.readline())


for _ in range(num):
    num_MBTI = int(sys.stdin.readline())
    MBTI_list = list(sys.stdin.readline().rstrip().split())

    answer = 0 if num_MBTI > 32 else float('inf')

    if answer != 0:
        for a, b, c in combinations(MBTI_list, 3):
            distance = count_diff(a, b) + count_diff(a, c) + count_diff(b, c)
            answer = min(answer, distance)

    print(answer)