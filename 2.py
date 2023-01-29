'''
2.write a programme that calculates and prints the value according to the given formula:
Q=Squarerootof[(2*C*D)/H]
following are the fixed values of C and H
C is 50. H is 30
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
let us assume the following comma separated input sequence is given to the program:
100,150,180
the output of the program should be
18,22,24
hints:
if the output received is in decimal form,it should be rounded off to it,s nearest value(for example,
ifthe output received is 26.0, it should be printed as 26)
in case of input data being supplied to the question,it should be assumed to be a console input
'''
import math
c=50
h=30
d=[int(input('n1')),int(input('n2')),int(input('n3'))]
new=[]
for i in d:

    Q=int(math.sqrt((2 *c * i)//h))
    new.append(Q)
print(new)