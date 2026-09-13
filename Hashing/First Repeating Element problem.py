class Solution():
    def firstRepeated(self, arr):
        s=set()
        answer=-1
        for i in range(len(arr)-1,-1,-1):
            if arr[i] not in s:
                s.add(arr[i])
            else:
                answer=i+1
        if answer!=-1:
            return answer
        else:
            return -1
x=Solution()
arr = [1, 5, 3, 4, 3, 5, 6]
arr2 = [1, 2, 3, 4]
print(x.firstRepeated(arr))
print(x.firstRepeated(arr2))

        
           
                
