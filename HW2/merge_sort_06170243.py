class Solution:
    def merge_sort(self,nums):
        self.nums = nums
        if len(nums) > 1:
            mid = len(nums)//2          ##找到最中間的數字
            left = nums[:mid]           ##把元素分成左邊和右邊
            right = nums[mid:]
        
            mergesort(left)             ##重複呼交merge把left和right繼續分成兩個
            mergesort(right)
        
            i = 0
            j = 0
            k = 0
            l = len(left)
            r = len(right)

            while i < l and j < r:       ##開始進行merge比較大小然後合併
                if left[i] < right[j]:   
                    nums[k] = left[i]
                    i += 1
                elif left[i] > right[j]:
                    nums[k] = right[j]
                    j += 1
                k += 1
            while i < l:                 ##把剩下還沒比較的元素放進list裡面
                nums[k] = left[i]        
                i += 1
                k += 1
            while j < r:
                nums[k] = right[j]
                j += 1
                k += 1

            return nums

##參考網站 https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
