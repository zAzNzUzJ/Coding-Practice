
# x=int(input())
# y=int(input())

#Note : The Honey Comb Structure input coloums should be a odd number  such that a complete honey comb structure

#Getting input from the use 

n=input().split()
x=int(n[0])
y=int(n[1])
row = x*2 +1 #split a single comb structure array representaion with min -3 row  
col = y*2 +1 #single comb structure array representaion with min -3 colum - always odd rows n col

#initially created a matrix frame temp - matrix create a structure

matrix = [[str(0) for x in range(col)] for y in range(row)]
# creates a dummy matrix of size - row X col
#iterate through the loop and replace the required pattern
#------------initially pattern differe for jthe 0th row - all the ODD and EVEN row are looped those are repeated
for i in range(1,row):
    for j in range(0,col,4):#replace the pattern at 4th  hop
        if i %2==0 and j !=col-1: # pattern for even number
            matrix[i][j]="\\"
            matrix[i][j+1]="___"
            matrix[i][j+2]="/"
            if j!=0:
                matrix[i][j-1]="   "
        else :            # pattern for even number
            matrix[i][j]="/"
            matrix[i][j+1]="   "
            matrix[i][j+2]="\\"
            if j!=0:
                matrix[i][j-1]="___"
        if j%2==0:          #pattern for the Zero 0 row 
            matrix[0][j]=" "
            matrix[0][j+1]="___"
            matrix[0][j+2]=" "
            if j!=0:
                matrix[0][j-1]="   "
                
#print the array matrix - to form a honey comb pattern               
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end="")
    print("")          
        


# for j in range(0,col,2):
#     matrix[0][j]=" "
# for j in range(1,col,4):
#     matrix[0][j]="___"
# for j in range(3,col,4):
#     matrix[0][j]="   "
    

# for j in range(0,col):
#     if j%2==0:
#         matrix[0][j]=" "
#     else:
#         matrix[0][j]="___"
# for j in range(3,col,4):
#     matrix[0][j]="   "
        
    


    
            
