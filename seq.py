num1 = input('\nNumber 1 (0-1000): ')
if num1 < 0 or num1 > 1000 :
    num1 = 0

num2 = input('Number 2 (0-1000): ')
if num2 < 0 or num2 > 1000 :
    num2 = 1

print "\nHow long do you want the sequence? (2-1000)"
count = input()
if count < 2 or count > 1000 :
    count = 10

seq = [num1,num2]
for x in range(count - 2):
    seq.append(seq[-1]+seq[-2])

print '\nSequence:'
output = ""
for number in seq:
    output += str(number) + "\n"

print output
