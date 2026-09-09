class Solution():
    def  findUnion(self,a,b):
       s=set(a)
       result=list(s)
       for i in range(len(b)):
            if b[i] not in s:
                s.add(b[i])
                result.append(b[i])
       return result
x=Solution()
a = [1, 2, 3]
b= [4, 5, 6] 
a1 = [1, 2, 3, 2, 1]
b1= [3, 2, 2, 3, 3, 2]
print(x.findUnion(a,b))
print(x.findUnion(a1,b1))