# def testGrid(): # Used in Week 1
#     grid = [ [1] * 10 for row in range(10) ]
#     grid[0][2] = 2
#     grid[0][3] = 2
#     grid[0][4] = 2
#     grid[2][7] = 2
#     grid[3][7] = 2
#     grid[4][7] = 2
#     # grid[0][1] = 2
#     # grid[1][1] = 2
#     # grid[2][1] = 2
#     # grid[1][4] = 2
#     # grid[1][5] = 2
#     # grid[1][6] = 2
#     # grid[4][5] = 2
#     # grid[4][6] = 2
#     # grid[4][7] = 2
#     # grid[6][5] = 2
#     # grid[6][6] = 2
#     # grid[6][7] = 2
#     # grid[6][2] = 2
#     # grid[7][2] = 2
#     # grid[8][2] = 2
#     return grid
    # print("... done!")
import tkinter as tk
import battleship_tests as test
def draw(canvas):
    pass
def makecanvas(w,h):
    root = tk.Tk()
    canvas = tk.Canvas(root,width=w,height=h)
    canvas.create_rectangle(0, 0, 500, 500)
    grid = test.testGrid()
    for i in range(10):
        for j in range(10):
            if grid[i][j]==2:
               canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50,fill="yellow")
            else:
               canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50,fill="blue")    
    canvas.pack()
    draw(canvas)
    root.mainloop()
makecanvas(500,500)




    #  canvas.create_rectangle(50, 100, 150, 200)