height = int(input("Height: "))

#Pyramid 
for rows in range(height):
    print(" "*(height-rows-1),end="")
    print("#"*(rows+1),end="")
    print("  ",end="")
    print("#"*(rows+1))
  
    