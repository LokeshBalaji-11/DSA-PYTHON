class Solution():
    def  myAtoi(self,s):
        i=0
        value=0
        sign=1
        while i<len(s) and s[i]==" ":
            i+=1
        if i<len(s) and s[i]=="-":
            sign=-1
            i+=1
        elif i<len(s) and s[i]=="+":
            sign=+1
            i+=1
        while i<len(s) and "0"<= s[i]<="9":
            b=ord(s[i])-ord("0")
            value=value*10+b
            i+=1
        value=value*sign
        if value > 2147483647:
            return 2147483647
        elif value<-2147483648:
            return -2147483648
        return value
a=Solution()
s = "-123"
s2= " 1231231231311133"
print(a.myAtoi(s))
print(a.myAtoi(s2))


    
            

            