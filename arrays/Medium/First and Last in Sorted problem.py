class Solution():
    def find(self,arr,x):
        low=-1
        high=-1
        for i in range(len(arr)):
            if arr[i]==x:
                if low==-1:
                  low =i
                  high=i
                elif low!=-1:
                   high=i
                
        return[low,high]
a=Solution()
arr1 = [1, 3, 5, 5, 5, 5, 67, 123, 125]
x1= 5
arr2 =[ 1, 3, 5, 5, 5, 5, 7, 123, 125]
x = 7

print(a.find(arr1,x1))
print(a.find(arr2,x))

