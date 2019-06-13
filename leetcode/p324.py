from typing import List


class Solution:
    """
    大小不等的不满足条件，经过交换会产生效果，但是对于大小相等的元素不适用。

    要求时间 O(n)，空间 O(1) 是真的好难想 ...

    思路：利用快排的思想得到 nums 的中位数，然后把小于中位数的数放在 (i & 1) == 0 的位置，大于中位数的数放在 (i & 1) == 1 的位置。
    """
    def wiggleSort(self, nums: List[int]) -> None:
        pass

    def mid_num(self, nums):
        pass

    def partition(self, nums):
        pivot = nums[0]
        i = 0
        for j in range(len(nums)):
            if nums[j] < pivot:
                i += 1



    def swap(self, nums, a, b):
        tmp = nums[a]
        nums[a] = nums[b]
        nums[b] = tmp


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2]
    # s.wiggleSort(nums)
    print(s.partition(nums))
    print(nums)
