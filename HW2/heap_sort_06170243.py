class Solution(object):
    def heap_sort(self,nums):
        self.nums = nums
        n = len(nums)

        for i in range(n, -1, -1):
            Solution().heapify(nums, n, i)

        for i in range(n-1, 0, -1):    
            nums[i], nums[0] = nums[0], nums[i]
            Solution().heapify(nums, i, 0)

        return nums

    def heapify(self,nums, n, i):
        large = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and nums[i] < nums[l]:
            large = l
        if r < n and nums[l] < nums[r]:
            large = r

        if large != i:
            nums[i], nums[large] = nums[large], nums[i]

            Solution().heapify(nums, n, large)

            
##參考網址 https://www.geeksforgeeks.org/python-program-for-heap-sort/
