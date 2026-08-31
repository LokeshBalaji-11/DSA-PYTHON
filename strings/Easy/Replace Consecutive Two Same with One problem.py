class Solution():
    def consecutive_character(self,s):
        consecutive=s[0]
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                pass
            else:
                consecutive+=s[i]
        return consecutive
a=Solution()
s= "aabb"
s2 = "aaaa"
s3= "aabaa"
print(a.consecutive_character(s))
print(a.consecutive_character(s2))
print(a.consecutive_character(s3))


            


    