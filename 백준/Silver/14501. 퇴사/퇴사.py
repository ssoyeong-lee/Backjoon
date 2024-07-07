from sys import stdin
input = stdin.readline

n = int(input())
t = []; p = []
for _ in range(n):
  ti, pi = map(int, input().split())
  t.append(ti), p.append(pi)

dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
  if t[i] + i <= n:
    dp[i] = max(dp[i + t[i]] + p[i], dp[i + 1])
  else:
    dp[i] = dp[i + 1]
print(dp[0])