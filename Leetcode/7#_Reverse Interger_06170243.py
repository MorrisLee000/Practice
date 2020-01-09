class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))
        r = int(s[::-1])
        if r > 2**31-1:
            return 0
        else:
            if x > 0:
                return r
            else:
                return -1 * r
