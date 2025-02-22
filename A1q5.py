file=open('mbox-short.txt')
count=0
email_list=[]
for line in file:
    line=line.strip()
    if line.startswith('From'):
        count +=1
        words=line.split()
        if words[1] not in email_list:
            email_list.append(words[1])

print(count)
print(email_list)