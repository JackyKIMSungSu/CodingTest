import sys

lcs1 = sys.stdin.readline().rstrip()
lcs2 = sys.stdin.readline().rstrip()

dp = [[0] * (len(lcs2) + 1) for _ in range((len(lcs1) + 1))]
for i in range(1, len(lcs1) + 1):
    for j in range(1, len(lcs2) + 1):
        if lcs1[i-1] == lcs2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(lcs1)][len(lcs2)])