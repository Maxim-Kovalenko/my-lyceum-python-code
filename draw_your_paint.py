import tkinter
print("To draw:hold LMB and move a mouse")
print("To change color:press one of colors on the left side")
window = tkinter.Tk()
canvas = tkinter.Canvas(window,  width=2000, height=2000, bg="white")
canvas.pack()
lastX, lastY = 0, 0
colour="black"
def store_position(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y
def on_click(event):
    store_position(event)
def on_drag(event):
    canvas.create_line(lastX, lastY, event.x, event.y, fill=colour, width=3)
    store_position(event)
canvas.bind("<Button-1>",on_click)
canvas.bind("<B1-Motion>",on_drag)
red_id = canvas.create_rectangle(10, 10, 30, 30, fill="red")
blue_id = canvas.create_rectangle(10, 35, 30, 55, fill="blue")
cyan_id = canvas.create_rectangle(10, 60, 30, 80, fill="cyan")
aquamarine_id = canvas.create_rectangle(10, 85, 30, 105, fill="aquamarine")
lime_id = canvas.create_rectangle(10, 110, 30, 130, fill="lime green")
white_id = canvas.create_rectangle(10, 135, 30, 155, fill="white")
def set_colour_red(event):
    global colour
    colour = "red"

def set_colour_blue(event):
    global colour
    colour = "blue"

def set_colour_cyan(event):
    global colour
    colour = "cyan"

def set_colour_aquamarine(event):
    global colour
    colour = "aquamarine"

def set_colour_lime(event):
    global colour
    colour = "lime green"

def set_colour_white(event):
    global colour
    colour = "white"
canvas.tag_bind(red_id, "<Button-1>",set_colour_red)
canvas.tag_bind(blue_id, "<Button-1>",set_colour_blue)
canvas.tag_bind(cyan_id, "<Button-1>",set_colour_cyan)
canvas.tag_bind(aquamarine_id, "<Button-1>",set_colour_aquamarine)
canvas.tag_bind(lime_id, "<Button-1>",set_colour_lime)
canvas.tag_bind(white_id, "<Button-1>",set_colour_white)
window.mainloop()