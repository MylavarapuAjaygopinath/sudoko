import numpy as np
s=[[8,0,0,1,3,4,9,0,2],
 [0,4,1,0,9,6,0,8,0],
 [0,0,5,0,7,0,0,1,0],
 [0,0,8,6,0,5,0,0,0],
 [4,0,6,3,1,0,0,0,9],
 [0,2,3,0,4,0,8,6,0],
 [5,0,0,7,0,9,0,0,0],
 [0,1,0,0,8,0,0,4,0],
 [0,0,0,4,0,1,0,0,6]]
def possible(x,y,val):
    for i in range(0,9):
        if s[x][i]==val:
            return False
    for i in range(0,9):
        if s[i][y]==val:
            return False
    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(3):
        for j in range(3):
            if s[x0+i][y0+j]==val:
                return False
    return True
def solve():
    for x in range(9):
        for y in range(9):
            if s[x][y]==0:
                for val in range(1,10):
                    if possible(x,y,val):
                        s[x][y]=val
                        solve()
                        s[x][y]=0
                return
    print(np.matrix(s))
solve()
