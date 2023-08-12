import turtle as t
import turtle
import random
import colorgram as cg


"""Import an image to extract the palette of color"""
color_list = cg.extract("HirstDotPainting.jpg", 6)
color_palette = []

for count in range(len(color_list)):
    rgb = color_list[count]
    color = rgb.rgb
    color_palette.append(color)

tim = t.Turtle()
tim.pensize(10)
tim.speed("fastest")
turtle.colormode(255)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angles = [90, 180, 270, 360]


def draw_geometry(num_sides):
    angle=360/num_sides
    for i in range(num_sides):
        tim.forward(80)
        tim.right(angle)
    num_sides += 1


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomcolor = (r, g, b)
    return randomcolor


def draw_random_line():
    while True:
        tim.color(random_color())
        tim.forward(25)
        tim.right(random.choice(angles))

def draw_multi_circle(num_circles):
    angle = 360 / num_circles
    current_angle = 0
    while current_angle <= 360:
        tim.color(random.choice(color_palette))
        tim.circle(100)
        tim.right(angle)
        current_angle+=angle
    print("Done")


def draw_hirstpainting(_num_dots, _painting_size):
    tim.screen.screensize(_painting_size, _painting_size)
    tim.penup()
    num_dots = _num_dots
    width = tim.screen.screensize()[0]
    height = tim.screen.screensize()[1]
    tim.setpos(-width/2, height/2)
    dx = width/num_dots
    dy = height/num_dots
    while tim.pos()[1] >= -height/2:
        print(f"Outside while loop {tim.pos()}")
        while tim.pos()[0] < width/2:
            tim.dot(20, random.choice(color_palette))
            if tim.pos()[0] != width:
                tim.forward(dx)
        tim.setpos(tim.pos()[0]-dx*num_dots, tim.pos()[1]-dy)
# draw_random_line()
# draw_multi_circle(10)
draw_hirstpainting(20, 500)

turtle.Screen().exitonclick()
