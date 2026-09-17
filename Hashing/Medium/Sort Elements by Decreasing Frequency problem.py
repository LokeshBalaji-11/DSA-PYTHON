class Solution():
    def sortByFreq(self,arr):
        f={}
        result=[]
        for i in range(len(arr)):
            if arr[i] not in f:
                f[arr[i]]=1
            else:
                f[arr[i]]+=1
        for ch, freq in sorted(f.items(), key=lambda x: (-x[1], x[0])):
            for i in range(f[ch]):
                result.append(ch)
        return result
x=Solution()
arr = [5, 5, 4, 6, 4]
arr1 = [9, 9, 9, 2, 5]
print(x.sortByFreq(arr))
print(x.sortByFreq(arr1))
    