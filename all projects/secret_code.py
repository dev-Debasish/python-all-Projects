# I tOWoveLlqo XOVouYH6k pmZIPILKYt

import random
import string


st = input("Enter the Message: ")
words = st.split(" ")

coding = input("1 for CODE OR. 0 gor DECODE: ")
coding = True if (coding == "1") else False
print(coding)


# coding part
if(coding):
    nWords = []
    for word in words:
        if(len(word) >= 3):
            r1 = "".join(random.choices(string.ascii_letters + string.digits, k=3))
            r2 = "".join(random.choices(string.ascii_letters + string.digits, k=3))
            new_st = r1 + word[1: ] + word[0] + r2
            nWords.append(new_st)
        else:
            nWords.append(word[::-1])
    print(" ".join(nWords))
# decoding part
else:
    nWords = []
    for word in words:
        if(len(word) >= 3):
            new_st = word[3:-3] 
            new_st = new_st[-1] + new_st[:-1]
            nWords.append(new_st)
        else:
            nWords.append(word[::-1])
    print(" ".join(nWords))
        



