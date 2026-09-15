class Solution():
    def nonRepeatingChar(self,s):
        f={}
        for ch in s:
            if ch in f:
                f[ch]+=1
            else:
                f[ch]=1
        for ch in s:
             if f[ch]==1:
                return ch
        return "$"
x=Solution()
s = "geeksforgeeks"
s1 = "aabbccc"
print(x.nonRepeatingChar(s))
print(x.nonRepeatingChar(s1))