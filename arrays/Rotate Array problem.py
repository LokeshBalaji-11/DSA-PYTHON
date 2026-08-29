class Solution():
    def rotate_array(self,arr,d):
        rotate=d%len(arr)
        result=arr[rotate:]+arr[:rotate]
        return result
    
arr1 = [1, 2, 3, 4, 5]
d1 = 2
arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
d2 = 3
arr3 = [7, 3, 9, 1]
d3= 9
a=Solution()
b=Solution()
print(a.rotate_array(arr1,d1))
print(a.rotate_array(arr2,d2))
print(b.rotate_array(arr3,d3))



