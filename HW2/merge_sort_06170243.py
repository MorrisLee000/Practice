class Solution(object):
    def merge_sort(self,nums):
        self.nums = nums
        if len(nums) > 1:
            mid = len(nums)//2          ##找到元素數量值的一半
            left = nums[:mid]           ##把元素分成左邊和右邊，因為mergesort是分成一半，所以先找出mid很重要
            right = nums[mid:]
        
            mergesort(left)             ##重複呼交merge把left和right繼續分成兩個
            mergesort(right)
        
            i = 0
            j = 0
            k = 0
            l = len(left)
            r = len(right)

            while i < l and j < r:       ##開始進行merge比較大小然後合併，假設left[i] == right[j]先把left[i]放進list裡面。
                if left[i] < right[j]:   
                    nums[k] = left[i]
                    i += 1               ##i++,j++,k++是用來代表位置，因為放進一個元素，如果不++會造成元素的放進去的元素被下一個取代
                elif left[i] > right[j]:
                    nums[k] = right[j]
                    j += 1
                elif left[i] == right[j]:
                    nums[k] = left[i]
                    i += 1
                k += 1
            while i < l:                 ##把剩下還沒比較的元素放進list裡面，剩下來的不分不用去比較大小，因為是其中一邊沒了才會有剩下來
                nums[k] = left[i]        ##的元素，直接放進list裡面，但還是要繼續k++
                i += 1
                k += 1
            while j < r:
                nums[k] = right[j]
                j += 1
                k += 1

            return nums

##參考網站 https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
