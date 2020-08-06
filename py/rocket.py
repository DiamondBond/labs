import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os, sys, subprocess

root = tk.Tk()
root.title("Rocket App Launcher")

def os_exec(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

apps = []

if os.path.isfile('applist.txt'):
    with open('applist.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir="/usr/share/applications/", title="Select File", filetypes=(("executables","*.desktop"), ("all files","*.*")))

    apps.append(filename)
    #print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="#f6f6f6")
        label.pack()

def delApp():
    for widget in frame.winfo_children():
        widget.destroy()

    if not apps:
        messagebox.showerror("Error", "No applications to remove.")
    else:
        apps.pop()
    for app in apps:
        label = tk.Label(frame, text=app, bg="#f6f6f6")
        label.pack()

def runApps():
    if not apps:
        messagebox.showerror("Error", "No applications to launch.")
    else:
        for app in apps:
            os_exec(app)


canvas = tk.Canvas(root, height=400, width=400, bg="#f6f6f6")
canvas.pack()

frame = tk.Frame(root, bg="#e5e5e5")
frame.place(relwidth=0.99, relheight=0.99, relx=0.005, rely=0.005)

openFile = tk.Button(root, text="Dock Application", padx=10, pady=5, fg="#000000", bg="#bdbdbd", command=addApp)
openFile.pack()

removeFile = tk.Button(root, text="Remove Application", padx=10, pady=5, fg="#000000", bg="#bdbdbd", command=delApp)
removeFile.pack()

runApps = tk.Button(root, text="Launch Applications", padx=10, pady=5, fg="#000000", bg="#bdbdbd", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('applist.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
