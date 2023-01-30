# Tetris running blocks through grid
# Turtle only stamping the colors based on the number in the grid
# Blocks falling as number in the grid

import turtle
import time


delay = 0.1  # For time/sleep

win = turtle.Screen()
win.title('TETRIS ONE BLOCKS by @DimaGutierrez')
win.bgcolor('black')
win.setup(400, 700)
win.tracer(0)
win.listen()

score_count = 0
score = turtle.Turtle()
score.color('red')
score.up()
score.hideturtle()
score.goto(60,-300)
score.write('Score: 0', align='center', font=('Courier', 24, 'normal'))



class Shape():
    def __init__(self, grid):
        self.x = 5
        self.y = 0
        self.color = 4
        self.grid = grid
        self.move = 'go'

    def move_right(self):
        if self.x < 11 and self.move == 'go':
            if grid[self.y][self.x+1]==0:
                grid[self.y][self.x]=0
                self.x += 1
                grid[self.y][self.x] = self.color

    def move_left(self):
        if self.x > 0 and self.move == 'go':
            if grid[self.y][self.x-1]==0:
                grid[self.y][self.x]=0
                self.x -= 1
                grid[self.y][self.x] = self.color
        

grid = [
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [4,3,3,1,0,1,0,3,3,4,0,1],
        [5,1,6,5,3,2,1,0,5,5,0,3],
        [1,2,3,4,5,2,0,4,2,3,0,4],
        [1,3,1,2,4,2,0,3,1,2,4,3],
        [1,1,2,3,0,2,2,2,0,3,0,1],
        [0,1,1,2,3,0,0,0,4,0,2,0],
        [2,0,1,2,3,0,6,5,5,5,0,2]
    ]

# Draw outline
border = turtle.Turtle()
border.pensize(10)
border.up()
border.hideturtle()
border.goto(-130,240)
border.down()
border.color('white')
border.rt(90)
border.fd(490) # Down
border.lt(90)
border.fd(260) # Right 
border.lt(90)
border.fd(490) # Up
border.up()
border.goto(0,260)
border.write("TETRIS", align='center', font=('Courier', 36, 'normal'))

pen = turtle.Turtle()
pen.up()
pen.speed(0)
pen.shape('square')
pen.shapesize(0.9, 0.9)
pen.setundobuffer(None)

def draw_grid(pen, grid):
    pen.clear()
    top = 230
    left = -110
    colors = ['black', 'red', 'lightblue', 'blue', 'orange', 'yellow', 'green',
              'purple']
    
    for y in range(len(grid)): # 24 rows
        for x in range(len(grid[0])): # 12 columns
            screen_x = left + (x*20) # each turtle 20x20 pixels
            screen_y = top - (y*20)
            color_number = grid[y][x]
            color = colors[color_number]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()


def check_grid():
    global score_count
    # Check if each row is full:
    for y in range(0,24):
        is_full = True
        y_erase = y
        for x in range(0,12):
            if grid[y][x] == 0:
                is_full = False
                break
        # Remove row and shift down
        if is_full:
            score_count += 1
            score.clear()
            score.write(f'Score: {score_count}', align='center', font=('Courier', 24, 'normal'))
            
            for y in range(y_erase-1, -1, -1):
                for x in range(0,12):
                    grid[y+1][x] = grid[y][x]

# Put shape in the grid   
shape = Shape(grid)
grid[shape.y][shape.x] = shape.color

# Draw grid
draw_grid(pen,grid)




# Main game loop
while True:
    win.update()
    
    # Move shape
    # Stop if at the bottom
    if shape.y == 23:
        shape.move = 'stop'
        check_grid()
        shape = Shape(grid)
        
    # Drop down one space if empty below
    elif grid[shape.y+1][shape.x] == 0: 
            grid[shape.y][shape.x]=0
            shape.y += 1
            grid[shape.y][shape.x] = shape.color
            
    # Stop if above another block
    else:
        shape.move = 'stop'
        shape = Shape(grid)
        check_grid()
        
    # Had to place it here for upcoming shapes...
    win.onkey(shape.move_right, 'Right')
    win.onkey(shape.move_left, 'Left')
 
    
    draw_grid(pen,grid)
    time.sleep(delay)
