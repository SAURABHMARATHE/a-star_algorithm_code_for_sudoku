
def check_validity(sudoku_arr,rowindex,colindex,possible_values,index,tempindex1,change_value_index):
    for i in range(0,9):
                            for j in range(0,9):    
                                        if sudoku_arr[i][j]==0:
                                            possible_values[tempindex1],index[tempindex1]=heuristic(sudoku_arr,i,j)
                                            rowindex[tempindex1]=i
                                            colindex[tempindex1]=j
                                            tempindex1+=1   
    count=0
    for i in range(0,tempindex1):
                        if index[i]==0:
                            count+=1
        
    if count==tempindex1:
            return 0
    else:
            return 1

def validate(sudoku_arr,rowindex,colindex,possible_values,index,tempindex2,change_value_index):
     #-----------------------------------------------------------------------------------

            
        possible_values[change_value_index].pop(0)
        
        return possible_values

    #---------------------------------------------------------------------------------    



#function that checks if all cells of sudoku board are filled with non-zero values
def check(sudoku_arr):
    count=0
    for i in range(0,9):
        for j in range(0,9):
            if sudoku_arr[i][j]!=0:
                count+=1

    if count==81:
        return 1
    else:
        return 0

#function to determine which square does the current cell lie in from 9 sub-sqaures of the sudoku board
def square_number(i,j):
    if i<=2 and j<=2:
        return 1
    elif i<=2 and j>=3 and j<=5:
        return 2
    elif i<=2 and j>=6:
        return 3
    elif i>=3 and i<=5 and j<=2:
        return 4
    elif i>=3 and i<=5 and j>=3 and j<=5:
        return 5
    elif i>=3 and i<=5 and j>=6:
        return 6
    elif i>=6 and j<=2:
        return 7
    elif i>=6 and j>=3 and j<=5:
        return 8
    elif i>=6 and j>=6:
        return 9    
    
#function to calculate heuristic associated with each cell(this is where A* in essence is implemented)
def heuristic(sudoku_arr,i,j):
    #values array will store 1 to 9
    values=[]
    #col_have_values will store values present already in column j of cell i,j
    col_have_values=[]
    #row_have_values will store values present already in row i of cell i,j
    row_have_values=[]
    #possible_values array will  store the values that are possible to be filled in cell i,j after eliminating\ 
    #row_have_values and col_have_values
    possible_values=[]
    
    #initializing all arays with appropriate values
    for x in range(0,9):
        values.append(x+1)
    for y in range(0,9):
        col_have_values.append(sudoku_arr[y][j])
    for z in range(0,9):
        row_have_values.append(sudoku_arr[i][z])
   
    
    index=0
    for x in range(0,9):
        for y in range(0,9):
            if values[x]==col_have_values[y] or values[x]==row_have_values[y]:
                values[x]=-1; #-1 means that value in values array cannot be used to fill cell i,j
   
    for x in range (0,9):
        if values[x]!=-1:
                possible_values.append(values[x])
                index+=1
   
    index2=0
    #final_possible_values will have the final values that can be filled in cell i,j after eliminating values from sub-square\
    #having cell i,j
    final_possible_values=[]
 
    square_no=square_number(i,j)
  
    if square_no==1:
        for z in range(0,len(possible_values)):
            for x in range (0,3):
                for y in range (0,3):
                    if x!=i or y!=j:
                        if sudoku_arr[x][y]==possible_values[z]:
                            possible_values[z]=-1 #-1 means that value on possible_values array which is there in sub-square of\
                                                  #cell i,j has been muted and cannot be used to fill cell i,j
                        
    elif square_no==2:
        for x in range (0,3):
            for y in range (3,6):
                for z in range(0,index):
                    if x!=i or y!=j:
                        if sudoku_arr[x][y]==possible_values[z]:
                            possible_values[z]=-1

    elif square_no==3:
        for x in range (0,3):
            for y in range (6,9):
                for z in range(0,index):
                    if x!=i or y!=j:
                        if sudoku_arr[x][y]==possible_values[z]:
                            possible_values[z]=-1                                        
                            
    elif square_no==4:
        for x in range (3,6):
            for y in range (0,3):
                for z in range(0,index):
                    if x!=i or y!=j:
                        if sudoku_arr[x][y]==possible_values[z]:
                            possible_values[z]=-1                            

    elif square_no==5:
        for x in range (3,6):
            for y in range (3,6):
                for z in range(0,index):
                    if x!=i or y!=j:
                        if sudoku_arr[x][y]==possible_values[z]:
                            possible_values[z]=-1                                                        
    elif square_no==6:
        for x in range (3,6):
            for y in range (6,9):
                for z in range(0,index):
                    if x!=i or y!=j:
                        if sudoku_arr[x][y]==possible_values[z]:
                            possible_values[z]=-1

    elif square_no==7:
        for x in range (6,9):
            for y in range (0,3):
                for z in range(0,index):
                    if x!=i or y!=j:
                        if sudoku_arr[x][y]==possible_values[z]:
                            possible_values[z]=-1        

    elif square_no==8:
        for x in range (6,9):
            for y in range (3,6):
                for z in range(0,index):
                    if x!=i or y!=j:
                        if sudoku_arr[x][y]==possible_values[z]:
                            possible_values[z]=-1                                                        

    elif square_no==9:
        for x in range (6,9):
            for y in range (6,9):
                for z in range(0,index):
                    if x!=i or y!=j:
                        if sudoku_arr[x][y]==possible_values[z]:
                            possible_values[z]=-1   
                                                  
    
    for z in range(0,index):
        if possible_values[z]!=-1:
            final_possible_values.append(possible_values[z])
            index2+=1
            
    #here index2 is the 'heuristic'. it is the length of the array final_possible_values i.e. it will tell no of values that can be filled\
    #in a cell
    return final_possible_values,index2
                                  
       
def main():
    #please initialize your sudoku_array here, '0' indicates empty cell
    sudoku_arr=[[1,0,0,5,6,0,7,2,0],[0,4,0,9,0,0,5,1,8],[0,0,5,0,1,0,9,3,6],[0,0,6,0,0,5,0,0,9],[8,1,9,3,0,0,6,5,2],[4,0,7,6,2,9,0,8,3],[5,0,0,7,4,0,2,9,0\
               ],[3,0,4,2,9,1,0,6,0],[0,2,1,8,5,6,0,4,7]]

    possible_values=[]  
    index=[]
    #rowindex and colindex will hold i,j values for each cell of sudoku that has to be filled
    rowindex=[]
    colindex=[]
    
                                
    stop_cond=0
    #cost calculates the cost or g(x) part of A*, while h(x) or heuristic is calulated by heuristic function
    cost=1
    heuristic_cost=0
    total_cost=0

    while stop_cond!=1:
        start=[0,0]
        temp=10
        tempindex=0
            
        for k in range (0,81):
                abc=[]
                for l in range(0,9):
                    abc.append(0)
                possible_values.append(abc)
                    
                
        
        for k in range (0,81):
                    index.append(0)
                    rowindex.append(0)
                    colindex.append(0)
                    
        for i in range(0,9):
                            for j in range(0,9):    
                                        if sudoku_arr[i][j]==0:
                                            possible_values[tempindex],index[tempindex]=heuristic(sudoku_arr,i,j)
                                            rowindex[tempindex]=i
                                            colindex[tempindex]=j
                                            tempindex+=1
                                            
        #find cell with minimum heuristic                                    
        change_value_index=0
        condition=0
        for i in range(0,tempindex):
                        if index[i]<temp and index[i]>0:
                            temp=index[i]
                            start=[rowindex[i],colindex[i]] 
                            change_value_index=i
        
        print "  "      
        print "cell selected"
        print start
        if index[change_value_index]==1:
            #cost+=1
            print "cost till current node %d"%total_cost  #total_cost till current node
            print "cost of going to current node %d"%cost
            heuristic_cost=index[change_value_index]
            print "heuristic cost of current node %d"%heuristic_cost
            total_cost+=cost+heuristic_cost #total_cost after adding cost and heuristic of current node
            print "total cost %d"%total_cost
            sudoku_arr[start[0]][start[1]]=possible_values[change_value_index][0]
            print sudoku_arr[start[0]][start[1]]
        else:
            while condition==0:
                sudoku_arr[start[0]][start[1]]=possible_values[change_value_index][0]
                condition=check_validity(sudoku_arr,rowindex,colindex,possible_values,index,0,change_value_index)
                if condition==0 and len(possible_values[change_value_index]) > 0:
                    possible_values=validate(sudoku_arr,rowindex,colindex,possible_values,index,0,change_value_index)                                                                                                                                                            
                    print change_value_index, possible_values[change_value_index]
                    sudoku_arr[start[0]][start[1]]=possible_values[change_value_index][0]
                #else:
                #    condition=1
            if condition==1:
                print "cost till current node %d"%total_cost  #total_cost till current node
                print "cost of going to current node %d"%cost
                heuristic_cost=index[change_value_index]
                print "heuristic cost of current node %d"%heuristic_cost
                total_cost+=cost+heuristic_cost #total_cost after adding cost and heuristic of current node
                print "total cost %d"%total_cost
                print sudoku_arr[start[0]][start[1]]
        
        #to check if sudoku is filled completey                                                                        
        stop_cond=check(sudoku_arr)

        if(stop_cond==1):
            
            for i in range(0,9):       
                print " "
                print sudoku_arr[i]
                
                
        
        
    


    
    
    