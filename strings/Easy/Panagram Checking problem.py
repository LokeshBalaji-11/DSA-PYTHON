class Solution():
    def check_panagram(self,s):
        con=s.lower()
        con=s.lower()
        a="abcdefghijklmnopqrstuvxyz"
        for ch in a:
            if ch not in con:
                return False
        return True
x=Solution()
s = "Bawds jog, flick quartz, vex nymph"
s1= "sdfs"
print(x.check_panagram(s))
print(x.check_panagram(s1))
