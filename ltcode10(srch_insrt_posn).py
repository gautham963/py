#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target in nums:
                val = nums.index(target)
                return val
                break
            elif (target not in nums):
                nums.append(target)
                nums.sort()
                val1 = nums.index(target)
                return val1
                break
