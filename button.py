import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text="Don't touch this button", width=40)
button.pack(padx=10, pady=10)
clickCount = 0
def onClick(event):
    global clickCount
    clickCount = clickCount + 1
    if clickCount == 1:
        button.configure(text="SERIOUSLY?I.SAID.DON'T.TOUCH.THIS.BUTTON!!!")
    elif clickCount == 2:
        button.configure(text="Are you normal?")
    elif clickCount == 3:
        button.configure(text="PLEASE STOP!!!")
    elif clickCount == 4:
        button.configure(text="Hah!Next time it will disappear!")
    else:
        button.pack_forget()
button.bind("<ButtonRelease-1>", onClick)
window.mainloop()
