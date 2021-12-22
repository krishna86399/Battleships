def checkShip(grid, ship):
    count=0
    for i in range(3):
        row=ship[i][0]
        col=ship[i][1]
        if grid[row][col]==1:
        # print(True)
           count=count+1
    # else: print (False)
    if count==3:
        return True
    # print("returning true")
    else:
        # print("returning false")
       return False

    
 