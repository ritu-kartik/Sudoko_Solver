board = [
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

###### THE ACTUAL ALGORITHM 
#this is the recursive algo which stops if the condition is met 
#find is the base case if it returns a solution 
def solve(bo):
    print(bo,"\n")
    find=find_empty(bo)
    if not find:
        return True
    else:
        row,col=find
    
    
    for i in range(1,10):
        if valid(bo, i, (row,col)): #we try adding the numbers from 1 to 10 by adding them 
            
            bo[row][col]=i #we add a new value here
            
            if solve(bo): #here we call the solution and then check if solve makes sense
                #and if solve does not make sense we go back again and get the right solution 
                #by resetting the value and following the recursive step 
                
                return True
            
            bo[row][col]=0
        
    return False








#########THIS BLOCK OF CODE HELPS ENTER THE BOX POSITIONS AND FIND THE VALUES AND CHECK IF THE VALUE HAS ALREADY BEEN INSERTED 
######### IF YES THE VALUE HAS BEEN INSERTED THEN IT IGNORES IT AND RETURNS FALSE BECAUSE IT DOES NOT WANT TO DUPLICATE THE VALS 

def valid(bo, num, pos):
    
    #Checking the row over here 
    for i in range(len(bo[0])):
        if bo[pos[0]][i]==num and pos[1] !=i: #this helps us check for other positions instead of the one JUST inserted.
            return False
        
    #Check the columns
    for i in range(len(bo)):
        if bo[i][pos[1]]==num and pos[0] !=i: #this helps us check for other positions instead of the one JUST inserted.
            return False
        
    #Check the box we are in (Segment)
    box_x=pos[1]//3 #// give us integer division vals 
    box_y=pos[0]//3
    #here we are looping through all the boxes to check for repettive elements
    
    for i in range(box_y*3, box_y*3 +3):
        for j in range(box_x*3, box_x*3 +3):
        #we will check the box we are in and multiply it by 3 rto get the element index
            if bo[i][j]==num and(i,j)!=pos:
                return False
            
    return True

       
    
    
################VISUAL OUTPUT- PRINTING THE BOARD ##########
def print_board(bo): #just prints the entire board with the ---- after every 3rd line 
    for i in range(len(bo)):
        if i % 3==0 and i != 0:
            print("- - - - - - - - - - - - - - -")
        
        for j in range(len(bo[0])): #every single position in the row is going to be checked to check if it is a multiple of 3 to draw the line 
            if j%3==0 and j!=0:
                print(" | ",end="")
                
            if j == 8:
                    print(bo[i][j])
            else:
                    print(str(bo[i][j])+" ",end="")
print_board(board)                    

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return(i,j) #row,col
    
    return None #returns none if there are no blank squares and calls the recursive algo 

print_board(board)
solve(board)
print("_________________________________\n___________________________________")
print_board(board)