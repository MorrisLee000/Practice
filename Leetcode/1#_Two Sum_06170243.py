class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        t = target
        n = len(nums)
        for i in range(n):
            s = t - nums[i]
            for j in range(n):
                if s == nums[j] and j != i:
                    l.append(i)
                    l.append(j)
                    return l
