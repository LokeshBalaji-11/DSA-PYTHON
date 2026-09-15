class Solution():
    def maxLength(self, arr):
        first={0:-1}
        total=0
        a=0
        for i in range(len(arr)):
            total+=arr[i]
            if total in first:
                length=i-first[total]
                a=max(a,length) 
            else:
                first[total]=i
        return a
x=Solution()
arr = [15, -2, 2, -8, 1, 7, 10, 23]
arr1 = [2, 10, 4]
print(x.maxLength(arr))
print(x.maxLength(arr1))