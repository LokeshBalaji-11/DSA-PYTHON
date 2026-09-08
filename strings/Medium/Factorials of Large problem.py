class Solution():
    def factorial(self, n):
        fac=1
        result=[]
        if n==1:
            result.append(n)
            return result
        else:
          for i in range(1,n+1):
               fac=fac*i
        fac=str(fac)
        for i in fac:
            result.append(int(i))
        return result
a=Solution()
n1=1
n2=10
n3=5
print(a.factorial(n1))
print(a.factorial(n2))
print(a.factorial(n3))