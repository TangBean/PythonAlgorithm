from math import log10, fmod

"""
n = 3^x
log3(n) = x -> 是个整数
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and fmod(log10(n) / log10(3), 1) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(81))
