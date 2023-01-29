'''
# 1.write a programme which takes 2 digits, x,y as input and generates a 2 dimensional array.the element
#value in the i-th row and j-th coloumn of the array should be i*j
note:i=0,1..,x-1; j=0,1,i-y-1
example
suppose the following inputs are given to the programme
3,5
then the output of the programme should be
[[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]]
hints: in case of input data being supplied to the question,it should be assumed to be a console input in a comma-
separated form.
'''
row_no=int(input("no of row:"))
col_no=int(input("no of col:"))
res=[[0 for col in range(col_no)] for row in range(row_no)]
for row in range(row_no):
    for col in range(col_no):
        res[row][col]=row*col
print(res)