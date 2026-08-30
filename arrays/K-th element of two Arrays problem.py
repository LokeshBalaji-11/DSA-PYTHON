class Solution():
    def kTh_element(self,a,b,k):
        combined= a+b
        combined.sort()
        return combined[k-1]
a1 = [2, 3, 6, 7, 9]
b1 = [1, 4, 8, 10]
k1= 5
a2= [1, 4, 8, 10, 12]
b2= [5, 7, 11, 15, 17]
k2= 6
x=Solution()
print(x.kTh_element(a1,b1,k1))
print(x.kTh_element(a2,b2,k2))