class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            s = str(x)
            r = int(s[::-1])
            if r == x:
                return True
            else:
                return False
