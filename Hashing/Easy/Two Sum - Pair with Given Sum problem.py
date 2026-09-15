class Solution():
    def twoSum(self, arr, target):
         value=0
         s=set()
         for i in range(len(arr)):
            value=target-arr[i]
            if value in s:
                return True
            s.add(arr[i])
         return False
a=Solution()
arr1 = [0, -1, 2, -3, 1]
target1 = -2
arr2 = [11]
target2 = 11
print(a.twoSum(arr1,target1))
print(a.twoSum(arr2,target2))
