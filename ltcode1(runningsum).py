#running sum problem Leet Code problem number 1480
from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        result = []

        for num in nums:
            running_sum += int(num)
            result.append(running_sum)

        return result

solver = Solution()
input_nums = input().split()
output = solver.runningSum(input_nums)
print(output)
