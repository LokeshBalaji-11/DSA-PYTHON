class solution():
    def reverse_words(self,st):
        word=st.replace("."," ")
        words=word.split()
        result=""
        for i in range(len(words)-1,-1,-1):
            result=result+words[i]
            if i!=0:
                result+="."
        return result
a=solution()
b="i.like.this.program.very.much"
print(a.reverse_words(b))

             
