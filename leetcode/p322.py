from typing import List
import sys

"""
DP，往 DP 想。

在设计 DP 时，我们只是要算 amount == a 处的值，而 amount < a 的最优解我们已经都算出来了，
那么 amount == a 处有哪些可能呢？答案就是 amount - coins[i]，遍历一下取最小就可以了。
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [-1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            cur = sys.maxsize
            for coin in coins:
                if a - coin >= 0 and dp[a - coin] != -1:
                    cur = min(cur, dp[a - coin])
            if cur != sys.maxsize:
                dp[a] = cur + 1

        return dp[amount]


if __name__ == '__main__':
    s = Solution()
    coins = [3, 7, 405, 436]
    amount = 8839
    print(s.coinChange(coins, amount))

