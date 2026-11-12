import turtle
import math
import pyautogui
import mouse


# function that draws the main menu
def drawMenu():
    # sets speed and size of turtle
    turtle.tracer(0)
    t = turtle.Turtle()
    t.speed(0)
    # t.hideturtle()
    t.pensize(2)

    t.penup()
    t.goto(-100, 100)
    t.pendown()

    for j in range(3):
        t.pencolor("black")
        t.fillcolor("cornflowerblue")
        t.begin_fill()
        for i in range(2):
            t.forward(200)
            t.right(90)
            t.forward(50)
            t.right(90)
        t.end_fill()
        t.penup()
        t.right(90)
        t.forward(100)
        t.left(90)
        t.pendown()

    t.penup()

    t.goto(0, 65)
    t.left(90)
    t.write("levels", align="center", font=("Courier", 12, "bold"))

    t.goto(0, -35)
    t.left(90)
    t.write("custom", align="center", font=("Courier", 12, "bold"))

    t.goto(0, -135)
    t.left(90)
    t.write("tutorial", align="center", font=("Courier", 12, "bold"))


# function that draws the custom map creator
def drawMap():
    # sets speed and size of turtle
    turtle.tracer(0)
    t = turtle.Turtle()
    t.speed(100)
    t.hideturtle()
    t.pensize(2)

    # gets dimensions of map
    global size
    global rows
    global columns

    # gets map data
    global content
    colours = {"w": "blue", "l": "lime", "h": "darkgreen", "f": "darkslategrey", "s": "brown", "e": "cadetblue"}

    square_counter = 0
    square_colour = content[square_counter]

    for row in range(rows):
        for col in range(columns):
            # finds the bottom left corner of current square, starting at bottom left of map
            x = col * size - (columns * size) / 2
            y = row * size - (rows * size) / 2

            # goes to square
            t.penup()
            t.goto(x, y)
            t.pendown()

            # draws square blue with black outline
            t.pencolor("black")
            t.fillcolor(colours[square_colour])
            if square_counter != rows * columns - 1:
                square_counter += 1
                square_colour = content[square_counter]
            t.begin_fill()
            for _ in range(4):
                t.forward(size)
                t.left(90)
            t.end_fill()

    # finds the bottom of the map
    t.penup()
    t.goto(-165, 0 - ((rows * size) / 2) - 30)
    t.pendown()

    # draws the 6 coloured cells
    colours = ["blue", "lime", "darkgreen", "darkslategrey", "brown", "cadetblue"]
    for i in range(6):
        t.pendown()
        t.pencolor("black")
        t.fillcolor(colours[i])
        t.begin_fill()

        for _ in range(4):
            t.forward(size)
            t.right(90)

        t.end_fill()
        t.penup()
        t.forward(60)

    # finds each coloured cell and writes their name
    t.goto(-150, 0 - ((rows * size) / 2) - 30)
    t.left(90)
    t.write("water", align="center", font=("Courier", 8, "bold"))

    t.goto(-90, 0 - ((rows * size) / 2) - 30)
    t.left(90)
    t.write("low land", align="center", font=("Courier", 8, "bold"))

    t.goto(-30, 0 - ((rows * size) / 2) - 30)
    t.left(90)
    t.write("high land", align="center", font=("Courier", 8, "bold"))

    t.goto(30, 0 - ((rows * size) / 2) - 30)
    t.left(90)
    t.write("wall", align="center", font=("Courier", 8, "bold"))

    t.goto(90, 0 - ((rows * size) / 2) - 30)
    t.left(90)
    t.write("settlement", align="center", font=("Courier", 8, "bold"))

    t.goto(150, 0 - ((rows * size) / 2) - 30)
    t.left(90)
    t.write("earthquake", align="center", font=("Courier", 8, "bold"))

    # map creator title
    t.goto(0, (rows * size) / 2)
    t.left(90)
    t.write("Custom Level Maker", align="center", font=("Courier", 15, "bold"))


# defines behaviours of clicks
def clicked(x, y):
    global click_position
    global fillcolour
    global mapid
    click_position = (x, y)
    # print("Clicked at:", x, y)
    print(x)
    print(y)

    # detects if pressed on the coloured cells, and changes fill colour to them
    if (-165 < x < -135) & (0 - ((rows * size) / 2) - 60 < y < 0 - ((rows * size) / 2) - 30):
        fillcolour = "blue"
        mapid = "w"
        print("clicked blue colour mapid" + mapid)

    if (-105 < x < -75) & (0 - ((rows * size) / 2) - 60 < y < 0 - ((rows * size) / 2) - 30):
        fillcolour = "lime"
        mapid = "l"
        print("mapid" + mapid)

    if (-45 < x < -15) & (0 - ((rows * size) / 2) - 60 < y < 0 - ((rows * size) / 2) - 30):
        fillcolour = "darkgreen"
        mapid = "h"
        print("mapid" + mapid)

    if (15 < x < 45) & (0 - ((rows * size) / 2) - 60 < y < 0 - ((rows * size) / 2) - 30):
        fillcolour = "darkslategrey"
        mapid = "f"

    if (75 < x < 105) & (0 - ((rows * size) / 2) - 60 < y < 0 - ((rows * size) / 2) - 30):
        fillcolour = "brown"
        mapid = "s"

    if (135 < x < 165) & (0 - ((rows * size) / 2) - 60 < y < 0 - ((rows * size) / 2) - 30):
        fillcolour = "cadetblue"
        mapid = "e"

    # checks if clicked within map boundary
    if (0 - columns * size / 2 < x < columns * size / 2) & (0 - rows * size / 2 < y < rows * size / 2):

        # gets coordinates originating from bottom left of map
        selected_column = click_position[0] + columns * size / 2
        selected_row = click_position[1] + rows * size / 2

        # uses those coordinates round up to exact square clicked
        column = math.ceil((selected_column / (size * rows)) * rows)
        row = math.ceil((selected_row / (size * columns)) * columns)

        # finds index of square
        mapindex = (row * 15) - 15 + (column - 1)

        # print("mapindex" + str(mapindex))
        # print("mapid 2 " + mapid)

        # updates map when drawn on
        with open("map.txt", "r") as f:
            text = f.read()

        text = text[:mapindex] + mapid + text[mapindex + 1:]

        with open("map.txt", "w") as f:
            f.write(text)

        # calls painting turtle
        t = paint_turtle

        global last_tile

        # if tile already drawn recently, return
        current_tile = (row, column, fillcolour)
        if current_tile == last_tile:
            return
        last_tile = current_tile

        # goes to bottom left corner of square clicked
        t.penup()
        t.goto(0 - columns * size / 2 + ((column - 1) * size), 0 - rows * size / 2 + ((row - 1) * size))

        # draws square with selected fill colour
        t.pendown()
        t.pencolor("black")
        t.fillcolor(fillcolour)
        t.begin_fill()
        t.setheading(0)

        for _ in range(4):
            t.forward(size)
            t.left(90)

        t.end_fill()

        screen = turtle.Screen()
        screen.tracer(0)

# ===========================================================================================


# sets map dimensions
size = 20
rows = 10
columns = 15

# opens file and sets data as "content"
with open("map.txt", "r", encoding="utf-8") as file:
    content = file.read().replace("\n", "")

#print(content[149])



drawMap()
# drawMenu()


# initial click position is none and default fill colour and mapid is lime
click_position = None
fillcolour = "lime"
mapid = "l"

# creates turtle used for painting on map
paint_turtle = turtle.Turtle()
paint_turtle.speed(0)
paint_turtle.hideturtle()
paint_turtle.pensize(2)

# last tile variable used to prevent repeated painting
last_tile = None


screen = turtle.Screen()
screen.tracer(0)
canvas = screen.getcanvas()

# ===========================================================================================


# function allows holding mouse down to draw
def drag(event):
    x = canvas.canvasx(event.x)
    y = -canvas.canvasy(event.y)
    clicked(x, y)


# release to stop drawing
def release(event):
    global last_tile
    last_tile = None


canvas.bind("<ButtonRelease-1>", release)
canvas.bind("<Button-1>", drag)
canvas.bind("<B1-Motion>", drag)


# updates screen on a short timer rather than instantly, prevents an error
def refresh():
    screen.update()
    screen.ontimer(refresh, 16)


refresh()
screen.mainloop()
