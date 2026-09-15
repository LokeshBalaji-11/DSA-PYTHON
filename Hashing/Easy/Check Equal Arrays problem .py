class Solution():
     def checkEqual(self, a, b):
          a.sort()
          b.sort()
          if a==b:
               return True
          else:
               return False
x=Solution()
a1 = [1, 2, 5]
b1 = [2, 4, 15]
a2 = [1, 2, 5, 4, 0] 
b2 = [2, 4, 5, 0, 1]
print(x.checkEqual(a1,b1))
print(x.checkEqual(a2,b2))