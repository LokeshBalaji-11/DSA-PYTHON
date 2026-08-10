class Solution():
    def reverse(self,arr):
       result=[]
       for i in range(len(arr)-1,-1,-1):
        result.append(arr[i])
       return result
arr = [1, 4, 3, 2, 6, 5]
arr2 = [4, 5, 2]
a=Solution()
b=Solution()
print(a.reverse(arr))
print(b.reverse(arr2))