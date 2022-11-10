
from random import choice, randint
from tkinter import *
from PIL import Image, ImageTk
width = 1080
height = 960
window = Tk()
ship_x = 1000
ship_y = 800
amount = 10
sonic = []
for _ in range(amount):
    sonic.append([randint(3, 10), randint(3, 10)])
image_names = ["asteroid1.png", "asteroid2.png", "asteroid3.png"]
images = [ImageTk.PhotoImage(Image.open("asteroid1.png").resize((100, 100))),
          ImageTk.PhotoImage(Image.open("asteroid2.png").resize((100, 100))),
          ImageTk.PhotoImage(Image.open("asteroid3.png").resize((100, 100)))]
space_img = ImageTk.PhotoImage(Image.open("space.png").resize((width, height)))
ship_img = ImageTk.PhotoImage(Image.open("spaceship.png").resize((80, 80)))

canvas = Canvas(width=width, height=height, bg="#111111")
canvas.create_image(0, 0, image=space_img, anchor=NW)
for _ in range(amount):
    canvas.create_image(1, 1, image=choice(images), anchor=NW)
canvas.create_image(1000, 800, image=ship_img, anchor=NW)


def image_move():
    global canvas
    global sonic
    global amount
    global ship_x
    global ship_y
    for i in range(amount):
        x, y = canvas.coords(i+2)
        if abs((ship_x + 40) - (x + 50)) < 90 and abs((ship_y + 40) - (y + 50)) < 90:
            window.destroy()
            break
        if x + 100 >= width:
            sonic[i][0] *= -1
        if y + 100 >= height:
            sonic[i][1] *= -1
        if x <= 0:
            sonic[i][0] *= -1
        if y <= 0:
            sonic[i][1] *= -1
        canvas.move(i+2, sonic[i][0], sonic[i][1])
    canvas.after(20, image_move)


def ship_move():
    global ship_x
    global ship_y
    global amount
    ship_x = window.winfo_pointerx() - window.winfo_rootx() - 40
    ship_y = window.winfo_pointery() - window.winfo_rooty() - 40
    if ship_y > height-80:
        ship_y = height-80
    if ship_x > width-80:
        ship_x = width-80
    if ship_x < 0:
        ship_x = 0
    if ship_y < 0:
        ship_y = 0
    canvas.moveto(amount+2, ship_x, ship_y)
    canvas.after(3, ship_move)


canvas.pack()

canvas.after(3, ship_move)
canvas.after(20, image_move)
mainloop()
