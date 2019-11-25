import tkinter as tk
import configparser
 
config = configparser.ConfigParser()
config.read('Config.ini')

bw, bh = int(config['Offset']['width']), int(config['Offset']['height'])
w, h = int(config.get('Size', 'width')), int(config.get('Size', 'height'))
fh = int(config.get('Gradient', 'height'))
count = int(fh/int(config.get('Gradient', 'level')))

windowsList = []
def destroyAllWindow(event):
    for window in windowsList:
        window.destroy()
    root.destroy()

root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', 1)
root.geometry('+'+str(bw)+'+'+str(920-h+fh))
canvas = tk.Canvas(root, bg="black", width=w, height=(h-fh), highlightthickness=0)
canvas.bind("<Button-1>", destroyAllWindow)
canvas.pack(fill='both')



for i in range(count):
    windowsList.append(tk.Tk())
    windowNow = windowsList[i]
    windowNow.overrideredirect(True)
    windowNow.attributes('-topmost', 1)
    windowNow.geometry('+'+str(bw)+'+'+str(int((920-h)+(fh/count)*i)))
    windowNow.attributes('-alpha', i*(1/count))
    canvas = tk.Canvas(windowNow, bg="black", width=w, height=(fh/count), highlightthickness=0)
    canvas.bind("<Button-1>", destroyAllWindow)
    canvas.pack(fill='both')


root.mainloop()