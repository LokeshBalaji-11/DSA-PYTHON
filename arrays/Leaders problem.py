class Solution():
    def Leaders(self,arr):
        largest=arr[-1]
        result=[]
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>=largest:
                largest=arr[i]
                result.append(arr[i])
        return result
arr=[16,17,4,3,5,2]
arr2=[10,4,2,4,1]
a=Solution()
b=Solution()
print(a.Leaders(arr))
print(b.Leaders(arr2))
