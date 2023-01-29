'''
4.write a programme which accepts a sequence of comma separated 4 digit binary numbers as
it,s input and then check wheather they are divisible by 5 or not. the numbers that are
divisible by 5 are to be printed in a comma separated sequence
example:
0100,0011,1010,1001
then the output should be:
1010
notes:assume the data is input by console
hints:in case of input data being supplied to the question,it should be assumed to be a console input
'''
m=list(input('enter 4digit no 0 to 1:').split(','))
for i in m:
    rang=int(i,2)
    if not rang%5:
        print(i)