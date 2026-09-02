class Solution():
    def rearrange(self,arr):
        d=[]
        a=len(arr)//2
        i=0
        j=len(arr)-1
        while i<j:
          d.append(arr[j])
          d.append(arr[i])
          i+=1
          j-=1
        if len(arr)%2!=0:
            d.append(arr[a])
        return d
a=Solution()
arr1 = [1, 2, 3, 4, 5, 6]
arr2= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
print(a.rearrange(arr1))
print(a.rearrange(arr2))