class Solution():
    def areRotations(self, s1, s2):
        if len(s1)!=len(s2):
            return False 
        return  s2 in s1+s1
a=Solution()
s1 = "abcd"
s2 = "cdab"
s3 = "abcd"
s4 = "acbd"
print(a.areRotations(s1,s2))
print(a.areRotations(s3,s4))

