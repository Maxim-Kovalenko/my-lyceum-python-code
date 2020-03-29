import tkinter
import random
gameOver = False
score = 0
squaresToClear = 0
def play_bombdodger():
    create_bombfield(bombfield)
    window = tkinter.Tk()
    layout_window(window)
    window.mainloop()
bombfield = []