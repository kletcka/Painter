
from tkinter import *
import tkinter.ttk as ttk
import tkinter.colorchooser
from PIL import ImageGrab
import time
import random
import math
root = Tk()
root.title("Canvas")
settings = Tk()
settings.title("Settings")
radius = 50
lis = []
main_color = "black"
minor_color = "white"
last_pos = None
counter = 0
size = 500
is_sprayed = False
is_piped = False


def reset():
    global main_color, minor_color, btn2, lbl1, lbl2, is_sprayed, btn7, is_piped, btn8, c, settings
    main_color, minor_color = "black", "white"
    lbl1["bg"] = main_color
    lbl2["bg"] = minor_color
    btn7["text"] = "Spray"
    is_sprayed = False
    btn8["text"] = "Pipe"
    is_piped = False
    c["bg"] = "white"
    settings.destroy()
    settings = Tk()
    restart()
    settings.after(1, retake)


def retake():
    global sca1, radius, label
    try:
        radius = int(sca1.get())

        if radius < 15:
            label["text"] = "·"
        else:
            if radius < 25:
                label["text"] = "•"
            else:
                if radius < 35:
                    label["text"] = "●"
                else:
                    if radius < 45:
                        label["text"] = "◉"
                    else:
                        label["text"] = "◯"
        settings.after(1, retake)
    except Exception:
        pass


def ask_for_color():
    global main_color, minor_color, btn2, lbl1, lbl2
    t = tkinter.colorchooser.askcolor()[1]
    if t != None:
        main_color = t
    lbl1["bg"] = main_color
    lbl2["bg"] = minor_color


def change_main_color():
    global main_color, minor_color, btn2, lbl1, lbl2
    main_color, minor_color = minor_color, main_color
    lbl1["bg"] = main_color
    lbl2["bg"] = minor_color


def paint_f(event):
    global c, last_pos
    if not is_sprayed:
        if last_pos == None:
            last_pos = (event.x, event.y)
        x = event.x
        y = event.y

        c.create_line(x, y, last_pos[0], last_pos[1],
                      fill=main_color, width=radius*1.01)
        if not is_piped:
            c.create_oval(last_pos[0]-(radius/2-0.5), last_pos[1]-(radius/2-0.5), last_pos[0]+(
                radius/2-0.5), last_pos[1]+(radius/2-0.5), fill=main_color, width=0)
            c.create_oval(x-(radius/2-0.5), y-(radius/2-0.5), x +
                          (radius/2-0.5), y+(radius/2-0.5), fill=main_color, width=0)
        last_pos = (event.x, event.y)
    else:
        for i in range(int(radius*4)):
            lengh = random.randint(0, int(radius*1.2))
            ugl = random.randint(0, 360)
            x = lengh * math.cos(ugl)
            y = lengh * math.cos(90-ugl)
            c.create_oval(event.x+x, event.y+y, event.x+x+1,
                          event.y+y+1, fill=main_color, width=0)


def cancel(event):
    global last_pos
    last_pos = None


def back():
    global c
    c["bg"] = tkinter.colorchooser.askcolor()[1]


def paint_s(event):
    global c, last_pos, is_piped, is_sprayed
    if not is_sprayed:
        if last_pos == None:
            last_pos = (event.x, event.y)
        x = event.x
        y = event.y
        c.create_line(x, y, last_pos[0], last_pos[1],
                      fill=minor_color, width=radius*1.01)
        if not is_piped:
            c.create_oval(x-(radius/2), y-(radius/2), x+(radius/2),
                          y+(radius/2), fill=minor_color, width=0)
            c.create_oval(last_pos[0]-(radius/2), last_pos[1]-(radius/2), last_pos[0] +
                          (radius/2), last_pos[1]+(radius/2), fill=minor_color, width=0)
        last_pos = (event.x, event.y)
    else:
        for i in range(int(radius*4)):
            lengh = random.randint(0, int(radius*1.2))
            ugl = random.randint(0, 360)
            x = lengh * math.cos(ugl)
            y = lengh * math.cos(90-ugl)
            c.create_oval(event.x+x, event.y+y, event.x+x+1,
                          event.y+y+1, fill=minor_color, width=0)


def save():
    global counter, settings
    settings.destroy()
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    x1 = x+500
    y1 = y+500
    ImageGrab.grab().crop((x, y, x1, y1)).save(f"image{counter}.jpg")
    counter += 1
    settings = Tk()
    restart()
    settings.after(1, retake)


def spray():
    global btn7, is_sprayed,  btn8, is_piped
    if btn7["text"] == "No Spray":
        btn7["text"] = "Spray"
    else:
        btn7["text"] = "No Spray"
    is_sprayed = not is_sprayed
    btn8["text"] = "Pipe"
    is_piped = False


def pipe():
    global btn7, is_sprayed,  btn8, is_piped
    if btn8["text"] == "No pipe":
        btn8["text"] = "Pipe"
    else:
        btn8["text"] = "No pipe"
    is_piped = not is_piped
    btn7["text"] = "Spray"
    is_sprayed = False


c = Canvas(root, width=500, height=500, bg='white')
c.grid(column=2, row=0, rowspan=60)


def restart():

    global btn, label, btn2, btn3, lbl1, lbl2, sca1, btn6, btn7, btn8, c
    settings.title("Settings")
    c.destroy()
    c = Canvas(root, width=500, height=500, bg='white')
    c.grid(column=2, row=0, rowspan=60)
    btn = Button(settings, text=" ☒ ", command=reset)
    btn.grid(column=5, row=0)
    label = Label(settings, text="·")
    label.grid(column=2, row=0)
    btn2 = Button(settings, text="  Replace   ", command=change_main_color)
    btn2.grid(column=3, row=0)
    btn3 = Button(settings, text="Choose color", command=ask_for_color)
    btn3.grid(column=4, row=0)
    lbl1 = Label(settings, text="            ", bg=main_color)
    lbl2 = Label(settings, text="            ", bg=minor_color)
    lbl1.grid(column=0, row=0)
    lbl2.grid(column=1, row=0)
    sca1 = Scale(settings, orient=HORIZONTAL, length=300,
                 from_=2, to=50, tickinterval=4, resolution=1)
    sca1.grid(column=0, row=3, columnspan=6)
    btn6 = Button(settings, text="Save", command=save)
    btn6.grid(column=0, row=7)
    btn7 = Button(settings, text="Spray", command=spray)
    btn7.grid(column=1, row=7)
    btn8 = Button(settings, text="Pipe", command=pipe)
    btn8.grid(column=2, row=7)
    btn9 = Button(settings, text="Background", command=back)
    btn9.grid(column=3, row=7)


restart()
root.bind("<B1-Motion>", paint_f)
root.bind("<ButtonRelease-1>", cancel)
root.bind("<B3-Motion>", paint_s)
root.bind("<ButtonRelease-3>", cancel)


settings.after(1, retake)
root.mainloop()
