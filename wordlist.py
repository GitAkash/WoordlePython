file = open('wordlist.txt','r')
content = file.read().splitlines()
words = set(content)
newfile = open('wordlist2.txt','w')

for word in words:
    if len(word) == 5 and word[0].islower() and word.isascii() and word.isalpha():
        newfile.write(word + '\n')

newfile.close()