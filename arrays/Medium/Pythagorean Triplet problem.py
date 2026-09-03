class Solution():
    def  pythagoreanTriplet(self,arr):
        c=0
        s=set(arr)
        for i in range(len(arr)):
           for j in range(i+1,len(arr)):
               c=arr[i]*arr[i]+arr[j]*arr[j]
               c=c**0.5
               if c in s:
                   return True
        return False
a=Solution()
arr = [3, 8, 5]
arr2=[3, 2, 4, 6, 5]
print(a.pythagoreanTriplet(arr))
print(a.pythagoreanTriplet(arr2))
