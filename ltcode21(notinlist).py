class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        Nums = []
        for i in range(0,len(nums)+1):
            Nums.append(i)

        setnums = set(nums)
        setNums = set(Nums)
        finalset =  setNums - setnums
        for i in finalset:
            return i
