class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val) != 0:
            for i in nums:
                if i == val:
                    nums.remove(i)
        return len(nums)
