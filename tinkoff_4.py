import math as m

if __name__ == '__main__':
    n = int(input())
    alpha = m.pi / n
    # area = 2 * r^2 * sin alpha * sin beta * sin gamma
    sins = [m.sin(alpha * i) for i in range(1, n)]
    r = 1 / 2 / sins[0]
    dp = [0, 0]
    for i in range(2, n):
        cand = dp[-1]
        for j in range(1, i):
            cand = max(cand, 2 * r * r * sins[j - 1] * sins[i - 1 - j] * sins[n - i - 1] + dp[max(0, j - 2)] + dp[max(0, i - j - 2)])
        dp.append(cand)

    best = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            best = max(best, 2 * r * r * sins[i-1] * sins[j - i - 1] * sins[n-j-1] + dp[max(0, i-2)] + dp[max(0, j-i-2)] + dp[max(0,n-j-2)])
    print(best)
