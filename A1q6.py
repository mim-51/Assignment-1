file=open('mbox.txt','r')
count=0
email_counts={}
for line in file:
    line=line.strip()
    if line.startswith('From'):
        words=line.split()
        if words[1] in email_counts:
            email_counts[words[1]]+=1
        else:
            email_counts[words[1]]=1
print(email_counts)