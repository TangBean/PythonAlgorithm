from typing import List


class Solution:
    # 气死了，中位数的方法怎么都搞不好 merge 那，先写个排序的，之后把中位数的补上
    def wiggleSort(self, nums: List[int]) -> None:
        tmp = sorted(nums)
        mid_index = int((len(nums) - 1) / 2)
        i, j, k = mid_index, len(nums) - 1, 0
        while i >= 0 and j > mid_index:
            nums[k] = tmp[i]
            nums[k+1] = tmp[j]
            k += 2
            i -= 1
            j -= 1
        if i == 0:
            nums[k] = tmp[i]

    # """
    # 大小不等的不满足条件，经过交换会产生效果，但是对于大小相等的元素不适用。
    #
    # 要求时间 O(n)，空间 O(1) 是真的好难想 ...
    #
    # 思路：利用快排的思想得到 nums 的中位数，然后把小于中位数的数放在 (i & 1) == 0 的位置，大于中位数的数放在 (i & 1) == 1 的位置。
    #
    # 在 merge 时的注意要点：要从尾开始取元素！
    # 如果从头取元素：4556 -> 4556，不会发生变化
    # 从尾取元素：4456 -> 5645，不会导致第二个元素和第三个元素相等
    # """
    # def wiggleSort(self, nums: List[int]) -> None:
    #     tmp = [0] * len(nums)
    #     for i in range(len(nums)):
    #         tmp[i] = nums[i]
    #     mid_index = self.mid_num(tmp)
    #     i, j, k = mid_index, len(nums)-1, 0
    #     while i >= 0 and j > mid_index:
    #         nums[k] = tmp[i]
    #         nums[k+1] = tmp[j]
    #         k += 2
    #         i -= 1
    #         j -= 1
    #     if i == 0:
    #         nums[k] = tmp[i]
    #
    # def mid_num(self, nums):
    #     N = len(nums)
    #     mid_index = int((N - 1) / 2)
    #     index = self.partition(nums, 0, N-1, mid_index)
    #     while index != mid_index:
    #         if index < mid_index:
    #             index = self.partition(nums, index+1, N-1, mid_index)
    #         else:
    #             index = self.partition(nums, 0, index-1, mid_index)
    #     return mid_index
    #
    # def partition(self, nums, lo, hi, pos):
    #     nums[lo], nums[pos] = nums[pos], nums[lo]
    #     i = lo
    #     for j in range(lo+1, hi+1):
    #         if nums[j] <= nums[lo]:
    #             i += 1
    #             nums[i], nums[j] = nums[j], nums[i]
    #     nums[lo], nums[i] = nums[i], nums[lo]
    #     return i


if __name__ == '__main__':
    s = Solution()
    # nums = [1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2]
    # nums = [1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2]
    # nums = [1, 5, 1, 1, 6, 4]
    # WA points
    # nums = [1, 3, 2, 2, 3, 1]
    # nums = [4, 5, 5, 6]
    nums = [5, 3, 1, 2, 6, 7, 8, 5, 5]

    # print(s.partition(nums, 0, len(nums)-1, 0))
    # s.mid_num(nums)
    # print(nums)

    s.wiggleSort(nums)
    print(nums)
