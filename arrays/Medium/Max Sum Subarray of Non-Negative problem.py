class Solution():
     def findSubarray(self, arr):
        current=0
        best=-1
        current_sub=[]
        total=0
        best_sub=[]
        for i in range(len(arr)):
            if arr[i]>=0:
                current+=arr[i]
                current_sub.append(arr[i])
            else:
                if(current>best) or (current==best and len(current_sub)>len(best_sub)):
                    best=current
                    best_sub=current_sub.copy()
                current_sub=[]
                current=0
        if(current>best) or (current==best and len(current_sub)>len(best_sub)):
                best=current
                best_sub=current_sub.copy()
        if best_sub==[]:
            return [-1]
        return best_sub
x=Solution()
arr = [1, 2, 3, -1, 6]
arr2= [-1, 2]
print(x.findSubarray(arr))  
print(x.findSubarray(arr2))              
             
