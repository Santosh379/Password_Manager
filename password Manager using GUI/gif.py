from tkinter import *
from PIL import Image, ImageTk

class Gif:
    def __init__(self, window, gif_path, bg='#f0f4f8', delay=20, size=(150, 150)):
        self.window = window
        self.gif = Image.open(gif_path)
        self.delay = delay
        self.frames = []
        self.size = size

        try:
            while True:
                frame = self.gif.copy().convert('RGBA')
                frame = frame.resize(self.size, Image.Resampling.LANCZOS)
                self.frames.append(ImageTk.PhotoImage(frame))
                self.gif.seek(len(self.frames))
        except EOFError:
            pass

        self.label = Label(window, bg=bg)
        self.label.config(image=self.frames[0])  # show first frame
        self.current_frame = 0
        self.animate()

    def animate(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.label.config(image=self.frames[self.current_frame])
        self.window.after(self.delay, self.animate)





