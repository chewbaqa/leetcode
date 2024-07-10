class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        l = []
        al = []
        
        for each in s:
            z = ord(each)
            l.append(z)

        for index in range(len(l) - 1):
            diff = l[index]-l[index+1]
            al.append(diff)

        for x in al:
            sum+=abs(x)
            
        return sum