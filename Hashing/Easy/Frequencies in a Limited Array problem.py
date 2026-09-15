class Solution():
    def frequencyCount(self, arr):
        f={}
        result=[]
        for i in range(len(arr)):
            if arr[i] in f:
                f[arr[i]]+=1
            else:
                f[arr[i]]=1
        for i in range(len(arr)):
            if i+1 in f:
                result.append(f[i+1])
            else:
                result.append(0)
        return result
x=Solution()
arr = [2, 3, 2, 3, 5]
arr2 = [3, 3, 3, 3]
print(x.frequencyCount(arr))
print(x.frequencyCount(arr2))