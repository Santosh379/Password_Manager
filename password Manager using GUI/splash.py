from tkinter import *
from gif import Gif

LABEL_FONT = ("Segoe UI", 14, "bold")
FONT = ("Segoe UI", 10)
# splash.py

def splash_screen(main_window):
    splash = Toplevel()
    splash.overrideredirect(True)
    splash.config(bg='#e6eff7')

    border_frame = Frame(splash, bg="#e6eff7", bd=0)
    border_frame.pack(padx=4, pady=4)

    label1 = Label(splash, text="🔐 Password Manager", font=("Segoe UI", 14, "bold"), bg='#e6eff7', fg="#1f2d3d")
    label1.pack(pady=10)

    # animated gif
    gif = Gif(window=splash, gif_path="assets/shield_front.gif", bg="#e6eff7",size=(140,140),delay=15)
    gif.label.pack()

    label2 = Label(splash, text="Loading...", font=("Segoe UI", 10), bg='#e6eff7', fg="#5a6b7a")
    label2.pack(pady=5)

    # center window
    splash.update_idletasks()
    width, height = 360, 240
    x = (splash.winfo_screenwidth() // 2) - (width // 2)
    y = (splash.winfo_screenheight() // 2) - (height // 2)
    splash.geometry(f"{width}x{height}+{x}+{y}")

    # hide main
    main_window.withdraw()
    total_time = int(len(gif.frames))*gif.delay*3

    def launch_main():
        splash.destroy()
        main_window.deiconify()


    main_window.after(total_time, launch_main)

