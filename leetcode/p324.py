from typing import List


class Solution:
    """
    大小不等的不满足条件，经过交换会产生效果，但是对于大小相等的元素不适用。

    要求时间 O(n)，空间 O(1) 是真的好难想 ...

    思路：利用快排的思想得到 nums 的中位数，然后把小于中位数的数放在 (i & 1) == 0 的位置，大于中位数的数放在 (i & 1) == 1 的位置。
    """
    def wiggleSort(self, nums: List[int]) -> None:
        n_2 = int((len(nums) + 1) / 2)
        self.mid_num(nums)
        if n_2 > 1:
            for i in range(1, n_2, 2):
                nums[i], nums[i+n_2] = nums[i+n_2], nums[i]

    def mid_num(self, nums):
        N = len(nums)
        mid_index = int((N - 1) / 2)
        index = self.partition(nums, 0, N-1, mid_index)
        while index != mid_index:
            if index < mid_index:
                index = self.partition(nums, index+1, N-1, mid_index)
            else:
                index = self.partition(nums, 0, index-1, mid_index)

    def partition(self, nums, lo, hi, pos):
        nums[lo], nums[pos] = nums[pos], nums[lo]
        i = lo
        for j in range(lo+1, hi+1):
            if nums[j] <= nums[lo]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[lo], nums[i] = nums[i], nums[lo]
        return i


if __name__ == '__main__':
    s = Solution()
    # nums = [1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2]
    # nums = [1, 5, 1, 1, 6, 4]
    nums = [1, 3, 2, 2, 3, 1]

    # print(s.partition(nums, 0, len(nums)-1, 0))
    # s.mid_num(nums)
    # print(nums)

    s.wiggleSort(nums)
    print(nums)
