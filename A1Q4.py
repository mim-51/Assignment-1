file=open('mbox-short.txt')

total=0.0
count=0

for line in file:
    if line.startswith("X-DSPAM-Confidence"):
        value=float(line.split(":")[1].strip())
        total +=value
        count += 1

if count>0:
    average=total/count
else:
    average=0.0

print(f"Average spam confidence: {average:.4f}")