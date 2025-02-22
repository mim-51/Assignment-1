def result(first_incourse, second_incourse, attendance, final):
    res = (first_incourse + second_incourse) / 2 + attendance + final
    return res

with open('mark.txt') as txt:
    marks = txt.readlines()

print('Roll', 'Letter Grade', 'Grade Point')
print('=== ==============  =========')

for line in marks:
    parts = line.strip().split('\t')  # Assuming the delimiter is tab
    roll, first_inc, second_inc, attendance, final = parts
    first_inc = int(first_inc)
    second_inc = int(second_inc)
    attendance = int(attendance)
    final = int(final)

    # Validation for correct input ranges
    if (int(roll) < 0 or first_inc < 0 or first_inc > 25 or 
        second_inc < 0 or second_inc > 25 or attendance < 0 or 
        attendance > 5 or final < 0 or final > 70):
        print('The number or roll is not correct!')
        continue

    ress = result(first_inc, second_inc, attendance, final)

    # Grade Calculation
    if ress >= 80:
        print(roll, 'A+', '4.00')
    elif ress >= 75:
        print(roll, 'A', '3.75')
    elif ress >= 70:
        print(roll, 'A-', '3.50')
    elif ress >= 65:
        print(roll, 'B+', '3.25')
    elif ress >= 60:
        print(roll, 'B', '3.00')
    elif ress >= 55:
        print(roll, 'B-', '2.75')
    elif ress >= 50:
        print(roll, 'C+', '2.50')
    elif ress >= 45:
        print(roll, 'C', '2.25')
    elif ress >= 40:
        print(roll, 'D', '2.00')
    else:
        print(roll, 'F', '0.00')
