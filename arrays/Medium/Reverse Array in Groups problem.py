class Solution():
    def reverse_In_Groups(self, arr, k):
         """code here"""
         if k>len(arr):
            reverse=[]
            for i in range(len(arr)-1,-1,-1):
                reverse.append(arr[i])
            arr[:]=reverse
            return arr
         else:
            value=[]
            for i in range(0,len(arr),k):
                for j in range(min(i+k,len(arr))-1,i-1,-1):
                    value.append(arr[j])
            arr[:]=value
            return arr
x=Solution()
arr1 = [1, 2, 3, 4, 5]
k1 = 3
arr2 = [5, 6, 8, 9] 
k2 = 5
print(x.reverse_In_Groups(arr1,k1))
print(x.reverse_In_Groups(arr2,k2))
        