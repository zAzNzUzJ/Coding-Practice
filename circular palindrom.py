#circular palindrom
#find the max len of the palindrom substring -- after each rotation in string
#MAX LENGTH OF THE PALIDROM SUBSTRING RETURNED -- FOR EVERY ROTATIONS

def circularPalindromes(s):
    
    l=len(s)
    Sub=[]
    lenofsub=[]
    Sub.append(s)
    for i in range(1,l):
        Sub.append(Sub[i-1][1:]+Sub[i-1][0])
    for i in range(l):
        temp=[]
        for x in range(l):
            for y in range(x+1,l+1):
                newsub=Sub[i][x:y]
                if newsub == newsub[::-1]:
                    temp.append(len(newsub))
             
        lenofsub.append(max(temp))
    return(lenofsub)
ST=input("Enter the string to  ")
result=circularPalindromes(ST)
for i in result:
    print(i)