class Solution():
    def firstElementKTime(self, arr,k):
        f={}
        for i in range(len(arr)):
            if arr[i] not in f:
                f[arr[i]]=1
            else:
                    f[arr[i]]+=1
            if f[arr[i]]==k:
                 return arr[i]
        return -1
x=Solution()
arr1 = [1, 7, 4, 3, 4, 8, 7]
k1 = 2
arr2 = [3, 1, 3, 4, 5, 1, 3, 3, 5, 4]
k2 = 3
arr3 = [10, 8, 2]
k3 = 10   
print(x.firstElementKTime(arr1,k1))
print(x.firstElementKTime(arr2,k2))
print(x.firstElementKTime(arr3,k3))   