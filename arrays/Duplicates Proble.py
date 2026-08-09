class solution():
    def Duplicates(self,arr):
        duplicate=[]
        s=set()
        for i in range(len(arr)):
            if arr[i] not in s:
                s.add(arr[i])
            else:
                duplicate.append(arr[i])
        return duplicate
x=[2,3,1,2,3]
b=[1,5,7,8]
ob=solution()
ob2=solution()
print(ob.Duplicates(x))
print(ob2.Duplicates(b))
