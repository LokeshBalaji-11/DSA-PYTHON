class Solution():
    def frequent_character(self,s):
        counts={}
        for ch in s:
            if ch not in counts:
             counts[ch]=1
            else:
                counts[ch]+=1
        max_count=0
        frequent=[]
        for i in counts:
            if counts[i]>max_count:
                max_count=counts[i]
        for ch in counts:
            if max_count==counts[ch]:
                frequent.append(ch)
        low=frequent[0]
        for i in range(len(frequent)):
            if frequent[i]<low:
                low=frequent[i]
        return low
a=Solution()
s = "testsample"
s1 = "output"
print(a.frequent_character(s))
print(a.frequent_character(s1))

