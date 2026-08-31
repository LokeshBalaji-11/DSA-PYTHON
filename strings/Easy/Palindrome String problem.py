class Solution():
    def palindrome(self,s):
        rev=""
        for i in range(len(s)-1,-1,-1):
            rev=rev+s[i]
        if rev==s:
            return True
        else:
            return False
a=Solution()
b=Solution()
s1="abba"
s2="abd"
print(a.palindrome(s1))
print(b.palindrome(s2))