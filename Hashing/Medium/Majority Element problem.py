class Solution():
     def findMajority(self, arr):
          m=len(arr)//3
          f={}
          count=0
          result=[]
          for i in range(len(arr)):
               if arr[i]  in f:
                    f[arr[i]]+=1
               else:
                   f[arr[i]]=1
          for ch in f:
               if f[ch]>m:
                    result.append(ch)
          result.sort()
          return result
x=Solution()
arr = [2, 2, 3, 1, 3, 2, 1, 1]
arr2 =  [3, 2, 2, 4, 1, 4]
print(x.findMajority(arr))
print(x.findMajority(arr2))