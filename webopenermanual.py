import webbrowser
from tkinter import *

companytype = ".com"

def myfunc():
    #----------------------------------Functions----------------------------------------
    def open():
        string = textbox.get()
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(string)
        exit()

    #----------------------------------Intro----------------------------------------
    root = Toplevel()
    root.title('Put the URL of the website:')
    root.geometry("320x320")
    background = PhotoImage( file = "chrome.png")

    mybg = Label(root, image = background)
    mybg.place(x = 0, y = 0)

    textbox = Entry(root, width=30)
    textbox.place(relx=0.68, rely=0.3, anchor=E)

    done = Button(root,text='done',command=open, bg = 'green', fg = 'white')
    done.place(relx=0.8, rely=0.3, anchor=W)

    root.mainloop()