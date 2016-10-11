print '\n\n*** FIBONACCI SEQUENCE GENERATOR ***\n\n  by Theodor Boending Hansen'

num1 = input('\nEnter the two numbers you want to start the sequence (From -1000 to 1000).\nFirst number (Traditionally 0 or 1):\t')
if num1 < -1000 or num1 > 1000 :
    num1 = 0

num2 = input('Second number (Traditionally 1):\t')
if num2 < -1000 or num2 > 1000 :
    num2 = 1

count = input("\nHow many terms to you want in the sequence? (From 2 to 100):\nTerms in sequence:\t\t\t")
if count < 2 or count > 100 :
    count = 10

seq = [num1,num2]
for x in range(count - 2):
    seq.append(seq[-1]+seq[-2])

print '\nSequence:'
output = ""
for x in seq:
    output += str(x) + "\n"

if seq[-2] != 0 :
    golden_ratio = float(seq[-1])/seq[-2]
else:
    golden_ratio = '----'
print output + '\nThe Golden Ratio calculated from last two terms (' + str(seq[-1]) + ' divided by ' + str(seq[-2]) + '):\n' + str(golden_ratio) + '\n\nReal value of The Golden Ratio:\n1.61803398875'
