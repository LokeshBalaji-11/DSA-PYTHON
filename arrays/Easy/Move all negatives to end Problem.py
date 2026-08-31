class Solution():
    def Move_negative(self,arr):
        result=[]
        for i in range(len(arr)):
            if arr[i] >=0:
                result.append(arr[i])
        for i in range(len(arr)):
            if arr[i]<0:
                result.append(arr[i])
        return result
arr = [1, -1, 3, 2, -7, -5, 11, 6 ]
arr2 = [-5, 7, -3, -4, 9, 10, -1, 11]
x=Solution()
y=Solution()
print(x.Move_negative(arr))
print(y.Move_negative(arr2))

