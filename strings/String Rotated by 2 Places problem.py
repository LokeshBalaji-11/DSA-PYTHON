class Solution():
    def isRotated(self,s1,s2):
        left=s1[2:]+s1[:2]
        right=s1[-2:]+s1[:-2]
        if s2 == right or  s2 == left:
              return True
        else:
            return False
a=Solution()
s1 = "geeksforgeeks"
s2 = "geeksgeeksfor"
s3 = "amazon"
s4 = "azonam"
print(a.isRotated(s1,s2))
print(a.isRotated(s3,s4))