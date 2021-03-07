import os
import threading
from datetime import datetime
import time
import tkinter as tk
import pyperclip

link = ""
link_time = ""
link_in_clipboard_flag = False


def check_clipboard():
    global link_in_clipboard_flag
    while 1:
        if "zoom.us" in pyperclip.paste():
            link_in_clipboard_flag = True
            return


def get_text():
    global link_time
    link_time = e2.get()
    global link
    link = str(e1.get())
    global master
    master.destroy()


master = tk.Tk()
master.title('auto zoom join by snir')
master.configure(background="#2A3240")
master.iconbitmap("your path to icon.ico")
ok_button = tk.Button(master, text='OK', command=get_text, width=3, height=1, font=("Consolas", 35))
ok_button.place(x=850, y=422)
ok_button.configure(background="#3EDB14", activebackground="#33CC78")
label_link = tk.Label(master, text="enter link:", height=5, font=("Consolas", 32))
label_link.grid(row=0)
label_link.configure(background="#2A3240")
label_time = tk.Label(master, text="enter time:", height=5, font=("Consolas", 32))
link_detected_label = tk.Label(master, text="", height=1, font=("Consolas", 26))
link_detected_label.place(x=250, y=260)
link_detected_label.configure(fg="green", background="#2A3240")
label_time.grid(row=1)
label_time.configure(background="#2A3240")
e1 = tk.Entry(master, font=("Consolas", 32), width="30")
e2 = tk.Entry(master, font=("Consolas", 32), width="30")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e1.configure(background="#39455B")
e2.configure(background="#39455B")

if "zoom.us" in str(pyperclip.paste()):
    link_in_clipboard_flag = True
    link = pyperclip.paste()
    print("got the link from the clipboard:", link)
    link_detected_label.configure(text="detected link from clipboard")
    e1.delete(0, tk.END)
    e1.insert(0, pyperclip.paste())

if not link_in_clipboard_flag:
    threading.Thread(target=check_clipboard).start()

while 1:
    master.update()
    master.after(10)
    if link_in_clipboard_flag:
        link_detected_label.configure(text="detected link from clipboard")
        e2.focus_force()
        e1.delete(0, tk.END)
        e1.insert(0, pyperclip.paste())
        break

tk.mainloop()

if "zoom.us" not in link:
    print("no valid link provided")
    quit()

if not link_time:
    print("no time provided")
    quit()

if link_time[1] == " ":
    link_time = "0" + link_time
print("time:", link_time.replace(" ", ":"))

while str(datetime.now())[11:-10] != link_time.replace(" ", ":"):
    time.sleep(1)

os.system(f"start {link}")
print("zoom meeting has started")
quit()
