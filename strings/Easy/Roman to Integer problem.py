class Solution():
    def roman_to_integer(self,s):
        result=0
        roman={
           "I":1,
           "V":5,
           "X":10,
           "L":50,
           "C":100,
           "D":500,
           "M":1000,}
        for i in range(len(s)):
          if i < len(s) - 1:
             if roman[s[i]] <roman[s[i+1]]:
              result = result - roman[s[i]]
             else:
               result = result + roman[s[i]]
        else:
          return result + roman[s[i]]
a=Solution()
x="IX"
y="XL"
s = "MCMIV"
print(a.roman_to_integer(x))
print(a.roman_to_integer(y)) 
print(a.roman_to_integer(s))            

