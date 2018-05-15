import turtle

def draw_triangle(some_turtle):
    for i in range(0,3):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_art():
    window =turtle.Screen()
    window.bgcolor('#b6b6b6')

    #create turtle pointer

    pointer = turtle.Turtle()
    pointer.speed(3)
    pointer.color('blue')

    for i in range(1,37):
        draw_triangle(pointer)
        pointer.right(10)
  
draw_art()
    
