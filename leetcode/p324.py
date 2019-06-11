from typing import List

'''
大小不等的不满足条件，经过交换会产生效果，但是对于大小相等的元素不适用。
'''

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for i in [x for x in range(20) if x % 2 == 0]:
            if i < len(nums) - 2:
                self.sortThree(nums, i, i+1, i+2)
            elif i == len(nums) - 2:
                self.sortTwo(nums, i, i+1)

    def sortThree(self, nums, i1, i2, i3):
        self.sortTwo(nums, i1, i2)
        self.sortTwo(nums, i3, i2)

    def sortTwo(self, nums, i1, i2):
        if nums[i1] > nums[i2]:
            self.swap(nums, i1, i2)

    def swap(self, nums, a, b):
        tmp = nums[a]
        nums[a] = nums[b]
        nums[b] = tmp


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,2,1,2,1,1,1,1,2,2,2]
    s.wiggleSort(nums)
    print(nums)
