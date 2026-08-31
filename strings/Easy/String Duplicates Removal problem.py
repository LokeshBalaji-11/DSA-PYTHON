class Solution():
    def duplicates(self,s1):
        result=""
        for i in range(len(s1)):
           if s1[i] not in result:
               result+=s1[i]
        return result
a=Solution()
s = "geEksforGEeks"
s2= "HaPpyNewYear"
print(a.duplicates(s))
print(a.duplicates(s2))