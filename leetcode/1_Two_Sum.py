# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_sorted = sorted(nums)
        start_idx = 0
        end_idx = len(nums) - 1

        while True:
            if nums_sorted[start_idx] + nums_sorted[end_idx] < target:
                start_idx += 1
            elif nums_sorted[start_idx] + nums_sorted[end_idx] > target:
                end_idx -= 1
            else:
                break
        a = nums_sorted[start_idx]
        b = nums_sorted[end_idx]
        if a == b:
            idx1 = nums.index(a)
            idx2 = nums.index(a, idx1+1)
            return [idx1, idx2]
        else:
            return [nums.index(a), nums.index(b)]


if __name__ == '__main__':

    print(Solution().twoSum([2, 5, 5, 11], 10))


# result
# Runtime: 20 ms, faster than 100.00% of Python online submissions for Two Sum.
# Memory Usage: 11.1 MB, less than 95.95% of Python online submissions for Two Sum.

