word=[]
teachers=open('amth.txt','r')

for line in teachers:
    if (not line.startswith("Applied mathematics")):
        line=line.strip()
        line=line.split()
        for list in line:
            if list not in word: #avoid duplicate
                word.append(list)

#print(word) 
word.sort()
print(word)