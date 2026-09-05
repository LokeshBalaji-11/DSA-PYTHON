class Solution():
    def isValid(self,s):
        num=s.split(".")
        if len(num)!=4:
            return False
        for i in num:
            if i=='':
                return False
            else:
              a=int(i)
            if len(i)==1 and i[0]=='0':
                pass 
            elif len(i)!=1 and i[0]=='0':
                return False
            if 0<=a<=255:
                pass
            else: 
                return False
        return True
a=Solution()
s = "222.111.111.111"
s2 = "5555..555"
print(a.isValid(s))
print(a.isValid(s2))