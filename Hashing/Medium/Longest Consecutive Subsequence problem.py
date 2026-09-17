class Solution():
    def longestConsecutive(self, arr):
        s=set(arr)
        current=0
        length=0
        a=-1
        for i in range(len(arr)):
            if arr[i]-1 not in s :
               current=arr[i]
               length=1
               while current+1 in s:
                   length+=1
                   current+=1
               a=max(a,length)
        return a
x=Solution()
arr = [2, 6, 1, 9, 4, 5, 3]
arr1 = [1, 9, 3, 10, 4, 20, 2]
print(x.longestConsecutive(arr))
print(x.longestConsecutive(arr1))