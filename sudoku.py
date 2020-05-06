board=[
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
      ]

def solve(bo) :

    find = find_empty(bo)

    if not find :
        return True
    else :
        row,col=find

    for i in range(1,10):
        if valid(bo,i,(row,col)) :
            
            bo[row][col]=i

            if solve(bo) :
                return True
        
            bo[row][col]=0
    return False     
                 

def valid(bo,num,pos):

    #column check
    for i in range(9):
        if bo[i][pos[1]]==num and i!=pos[0]:
            return False


    #row check
    for i in range(9):
        if bo[pos[0]][i]==num and i!=pos[1]:
            return False    
        

    #box check

    box_y= pos[0]//3        
    box_x=pos[1]//3

    for i in range(box_y*3,box_y*3 +3) :
        for j in range(box_x*3,box_x*3 +3) :
            if bo[i][j]==num and (i,j)!=pos :
                return False
            
    
    return True
    
def print_board(bo):

    print("\n---------------------")
    for i in range(len(bo)):
        for j in range(len(bo[0])):
                       if (j)%3==0 and j!=0:
                           print("|",end=" ")
                       print(bo[i][j],end=" ")
                       

        if (i+1)%3==0 and i!=0:
            print("\n---------------------\n")
        else:
            print("\n")
            
def find_empty(bo) :

    for i in range(9):
        for j in range(9):
            if bo[i][j]==0:
                return (i,j)
    return None 



            

print_board(board)
solve(board)
print_board(board)
    
    

















