print '\nFIBONACCI SEQUENCE GENERATOR'

num1 = input('\nEnter the number you want to start the sequence (Traditionally 0 or 1).\nFirst number (0-1000): ')
if num1 < 0 or num1 > 1000 :
    num1 = 0

num2 = input('\nEnter the second number of the sequence (Traditionally 1).\nSecond number (0-1000): ')
if num2 < 0 or num2 > 1000 :
    num2 = 1

count = input("\nHow long do you want the sequence to be? (2-100): ")
if count < 2 or count > 100 :
    count = 10

seq = [num1,num2]
for x in range(count - 2):
    seq.append(seq[-1]+seq[-2])

print '\nSequence:'
output = ""
for x in seq:
    output += str(x) + "\n"

print output
