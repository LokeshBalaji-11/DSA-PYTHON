class Solution():
    def round_To_Nearest(self,s):
        value=0
        a=int(s[-1])
        if a<5:
            return s[:-1]+"0"
        elif a>5:
           num=list(s[:-1])
           i=len(num)-1
           while  i>=0 and num[i]=='9':
               num[i]="0"
               i-=1
           if i>=0:
               num[i]=str(int(num[i])+1)
           else:
               num.insert(0,'1')
           return ''.join(num)+"0"
        elif a==5:
            return s[:-1]+"0"

a=Solution()
s = "29"
s2 = "15"
print(a.round_To_Nearest(s))
print(a.round_To_Nearest(s2)) 


        