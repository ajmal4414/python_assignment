'''
5.write a programme which will find all such numbers between 1000 and 3000(both included)such that each digit
of the number is an even number.
the numbers obtained should be printed in a comma-separated sequence on a single line
hints:
in case of input data being supplied to the question, it should be assumed to be a console input
'''
list=[]
for i in range(999,3001):
    s=str(i)
    if (int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0):
        list.append(s)
print(','.join(list))