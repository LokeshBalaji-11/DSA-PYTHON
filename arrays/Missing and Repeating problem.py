class Solution():
    def Missing(self,arr):
        s=set()
        result=[]
        for i in range(len(arr)):
            if arr[i] not in s:
                s.add(arr[i])
            elif  arr[i] in s:
                result.append(arr[i])
        for i in range( 1,len(arr)+1):
            if i not in s:
                result.append(i)
        return result
a=[2,2]
b=[1,3,3]
x=Solution()
y=Solution()
print(x.Missing(a))
print(y.Missing(b))

                 