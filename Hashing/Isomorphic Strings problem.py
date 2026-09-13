class Solution():
    def areIsomorphic(self, s1, s2):
        f={}
        s=set()
        for i in range(len(s1)):
            if s1[i] not in f:
                if s2[i] in s:
                    return False
                else:
                 f[s1[i]]=s2[i]
                 s.add(s2[i])
            else:
                if f[s1[i]]!=s2[i]:
                    return False
        return True
x=Solution()
s1 = "aab"
s2 = "xxy"
a = "aab"
b = "xyz"
s3 = "abc"
s4 = "xxz"
print(x.areIsomorphic(s1,s2))
print(x.areIsomorphic(a,b))
print(x.areIsomorphic(s3,s4))     