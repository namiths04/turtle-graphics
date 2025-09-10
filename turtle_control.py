import turtle
screen=turtle.Screen()
screen.title("move turtle with arrow keys")
player=turtle.Turtle()
player.shape('turtle')

#movement functions
def move_forward():
    player.forward(20)

def move_backward():
    player.backward(20)

def turn_left():
    player.left(20)

def turn_right():
    player.right(20)

#screen controls
screen.listen()
screen.onkey(move_forward , 'Up')
screen.onkey(move_backward , 'Down')
screen.onkey(turn_left , 'Left')
screen.onkey(turn_right , 'Right')

screen.mainloop()
