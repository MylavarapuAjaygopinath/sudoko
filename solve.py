import numpy as np
#Reading The Puzzle Row wise
s=[[int(i)for i in input().split()]for j in range(9)]
def validate(x,y,val):
    #This function is used to check whether the number 'val' is suitable to keep
    #at position 'i j' or not.
    for i in range(0,9):
        #checking whether the number is repeated in the row or not
        if s[x][i]==val:
            return False
    for i in range(0,9):
        #checking whether the number is repeated in the column or not
        if s[i][y]==val:
            return False
    #checking whether the number is repeated in sub box or not
    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(3):
        for j in range(3):
            if s[x0+i][y0+j]==val:
                return False
    #if not repeated in any of the cases then return true
    return True
def sudoko():
    for x in range(9):
        for y in range(9):
            if s[x][y]==0:
                #if the value in the cell is 0 then check for the suitable number
                for val in range(1,10):
                    if validate(x,y,val):
                        #if suitable then assign it in the cell
                        s[x][y]=val
                        sudoko()#for backtracking
                        s[x][y]=0
                return
    print("Answer is:")
    print(np.matrix(s))
sudoko()

