class Solution:
    def romanToInt(self, s: str) -> int:
        f = 0
        l = len(s)
        convert = {"M": 1000, "D": 500 , "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        for i in range(l-1):
            if convert[s[i]] < convert[s[i+1]]:                
                f -= convert[s[i]]            
            else:                
                f += convert[s[i]]        
        f += convert[s[-1]]        
        return f
