def print_pascal_triangle(height):
  
    res=[[1]]
    for i in range(height-1):

        temp = [0]+res[-1]+[0]
        new_row =[]
        
        for j in range(len(res[-1])+1):
            new_row.append(temp[j]+temp[j+1])
        res.append(new_row)
    
    for i in range(height):
        print(" "* (height-i),end=" ")
        for j in res[i]:
            print(j,end=" ")
        print("")
       

            

    

# print_pascal_triangle(10)
