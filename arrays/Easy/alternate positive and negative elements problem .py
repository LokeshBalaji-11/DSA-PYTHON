class Solution():
    def alternative(self,arr):
        n=[]
        p=[]
        for i in range(len(arr)):
            if arr[i] >=0 :
                p.append(arr[i])
            elif arr[i]<0:
                n.append(arr[i])
        i=0
        j=0
        result=[]
        while i<len(p) and j<len(n):
            result.append(p[i])
            result.append(n[j])
            i+=1
            j+=1
        while i<len(p):
            result.append(p[i])
            i+=1
        while j<len(n):
            result.append(n[j])
            j+=1
        return result
a=Solution()
b=Solution()
arr1 = [9, 4, -2, -1, 5, 0, -5, -3, 2]
arr2 = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print(a.alternative(arr1))
print(b.alternative(arr2))