#Day 7 Packages Can be downloaded by pypi.org installed in python folder 
from prettytable import PrettyTable
from turtle import Turtle,Screen
import colorgram

# Extract 6 colors from an image.
x = PrettyTable()

x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])

print(x)

timmyTurtle=Turtle()
timmyTurtle.forward(100)
timmyTurtle.left(90)
timmyTurtle.forward(100)
timmyTurtle.left(90)
timmyTurtle.forward(100)
timmyTurtle.left(90)
timmyTurtle.forward(100)
timmyTurtle.left(100)



#timmyTurtle.circle(10)
for i in range(10):
    timmyTurtle.forward(10)
    timmyTurtle.penup()
    timmyTurtle.forward(10)
    timmyTurtle.pendown()






colors = colorgram.extract('testimage.jpg',4)

print(colors)
