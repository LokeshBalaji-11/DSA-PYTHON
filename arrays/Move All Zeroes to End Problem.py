class Solution():
    def Move(self,arr):
        result=[]
        count=0
        for i in range(len(arr)):
            if arr[i]!=0 :
                result.append(arr[i])
            else:
                count= count+1
        for i in range(count):
            result.append(0)
        return result
arr1 = [1, 2, 0, 4, 3, 0, 5, 0]
arr2=[10, 20, 30]
a=Solution()
b=Solution()
print(a.Move(arr1))
print(b.Move(arr2))
