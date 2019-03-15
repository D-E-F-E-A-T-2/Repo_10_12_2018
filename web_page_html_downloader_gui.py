import urllib.request
def wp_downloader(self):
    global pb
    pb = ttk.Progressbar(bottomFrame,orient ="horizontal",length = 200, mode ="determinate")
    pb.pack()
    pb["maximum"] = 100
    pb["value"] = 100
    global give
    give = e1.get()
    try:
        url = urllib.request.urlopen(give)
        content = url.read()
    except urllib.error.HTTPError:
        print("Webpage not found")
        exit()
    f = open('reader.html', 'wb')
    f.write(content)
    f.close()

from tkinter import ttk
from tkinter import *
root = Tk()
root.geometry("500x150")
root.title("Web Page Downloader")
label = Label(root, text = "GUI for webpage_downloader.py")
label.pack()
topFrame = Frame(root)
topFrame.pack()
label = Label(topFrame, text = "This applications takes a link of a webpage that you want to download in html format.")
label.pack() # check side options here
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)
e1 = Entry(bottomFrame)
e1.pack()
e1.focus_set()
button1 = Button(bottomFrame, text="Click here!", fg="red", cursor = "pirate")
button1.bind("<Button-1>", wp_downloader)
button1.pack(fill='x')

root.mainloop()
