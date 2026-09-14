class Solution():
    def allPairs(self, target, arr1, arr2):
          # code here 
      pairs=[]
      view=0
      f={}
      s=set(arr2)
      for i in range(len(arr2)):
        if arr2[i] not in f:
            f[arr2[i]]=1
        else:
            f[arr2[i]]+=1
      for i in range(len(arr1)):
            view=target-arr1[i]
            if view in s:
                for j in range((f[view])):
                   pairs.append([arr1[i],view])
      pairs.sort()
      return pairs
x=Solution()
target = 9
a = [1, 2, 4, 5, 7]
b = [5, 6, 3, 4, 8]
target2 = 9
a1 = [1, 2, 4, 5, 7, 4]
b1 = [5, 6, 3, 4, 8, 4]
print(x.allPairs(target,a,b))
print(x.allPairs(target2,a1,b1))