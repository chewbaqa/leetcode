class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
    
        for index in range(len(s)-1):
            sum+= abs(ord(s[index]) - ord(s[index+1]))

        return sum