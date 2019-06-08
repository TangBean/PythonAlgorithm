from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        res = [0] * k
        for i in range(0, k + 1):
            j = k - i
            if i > len(nums1) or j > len(nums2):
                continue

            first = self.maxKNums(nums1, i)
            second = self.maxKNums(nums2, j)
            cur = self.merge(first, second)
            res = max(res, cur)
        return res

    def maxKNums(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * k
        j = 0
        for i in range(len(nums)):
            while len(nums) - i > k - j and j > 0 and res[j - 1] < nums[i]:
                j -= 1
            if j < k:
                res[j] = nums[i]
                j += 1
        return res

    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res_len = len(nums1) + len(nums2)
        res = [-1] * res_len
        i, j = 0, 0
        for k in range(res_len):
            if i == len(nums1) or (j < len(nums2) and nums2[j] > nums1[i]):
                res[k] = nums2[j]
                j += 1
            elif j == len(nums2) or (i < len(nums1) and nums1[i] > nums2[j]):
                res[k] = nums1[i]
                i += 1
            else:
                if self.compare(nums1, i, nums2, j):
                    res[k] = nums1[i]
                    i += 1
                else:
                    res[k] = nums2[j]
                    j += 1
        return res

    def compare(self, nums1: List[int], idx1: int, nums2: List[int], idx2: int) -> bool:
        while idx1 < len(nums1) and idx2 < len(nums2) and nums1[idx1] == nums2[idx2]:
            idx1 += 1
            idx2 += + 1
        return idx2 == len(nums2) or (idx1 < len(nums1) and nums1[idx1] > nums2[idx2])


if __name__ == '__main__':
    s = Solution()
    # nums1 = [3, 4, 6, 5]
    # nums2 = [9, 1, 2, 5, 8, 3]
    # k = 5
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    k = 5
    print(s.maxNumber(nums1, nums2, k))
