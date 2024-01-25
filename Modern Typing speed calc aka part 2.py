script = input("Enter the Sample text\t\t")
script = script.lower()
sample = script.split()
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
test = input("Type as much as you can\t\t")
test = test.lower()
text_test = test.split()
mistakes = len(text_test)
wordcount = len(text_test)

# kindly recheck the following piece of code in comments i.e. use different counters for both pieces of text and upon line skip, append the counter of sample text
line_miss = False
'''def my_marzi():
    print("I am running")
    global sample
    global text_test
    global c
    global i
    global line_miss
    line_miss = False'''




c = 0
i = 0
ghaltiyaan = dict()
while c < wordcount:
    line_miss = False
    if sample[i] == text_test[c]:
        mistakes = mistakes - 1
        c = c + 1
        i = i + 1
    if sample[i] != text_test[c]:
        ghaltiyaan[c] = ["word", c + 1, text_test[c]]
        c = c + 1
        i = i + 1

# reconstruct the following piece of code in comments to make it work

        '''for j in range(wordcount - i):
            if text_test[c] == sample[i + j + 1]:
                for k in range(wordcount - i):
                    print(i)
                    print(k)
                    print(c)
                    print(j)

                    if sample[i + k + 1] != text_test[c + j + 2 + k]:
                        c = c + 1
                        i = i + 1
                        if j > 0:
                            line_miss = True
                        i = i + j + 1

                        break
                    line_miss = True
                    if k == 22:
                        i = i + j + 1
        if line_miss:
            print("Some words or lines are overlooked or skipped from ", c, "th word to ", i, "th word; of the SAMPLE TEXT")'''


print("\t", mistakes, "mistakes")
for i in ghaltiyaan:
    print(ghaltiyaan[i])
