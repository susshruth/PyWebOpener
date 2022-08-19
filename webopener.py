from webopenermanual import myfunc
from tkinter import *
import webbrowser
import time

companytype = ".com"
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
#----------------------------------Functions----------------------------------------
def open():
    global chrome_path
    string = "http://" + textbox.get() + companytype
    webbrowser.get(chrome_path).open(string)
    exit()

def gfunc():
    global chrome_path
    string = "https://classroom.google.com/u/0/h"
    webbrowser.get(chrome_path).open(string)
    exit()

def lfunc():
    global chrome_path
    string = "https://leetcode.com/study-plan/"
    webbrowser.get(chrome_path).open(string)
    exit()

#----------------------------------Intro----------------------------------------
master = Tk()
master.title('Put the name of the website:')
master.geometry("320x320")
bg = PhotoImage(file = "chrome.png")

label1 = Label( master, image = bg)
label1.place(x = 0, y = 0)

textbox = Entry(master, width=30)
textbox.place(relx=0.68, rely=0.3, anchor=E)

companylabel = Label(master, text=".com")
companylabel.place(relx=0.73, rely=0.3, anchor=CENTER)

done = Button(master,text='done',command=open, bg = 'green', fg = 'white')
done.place(relx=0.8, rely=0.3, anchor=W)

#----------------------------------Type----------------------------------------
def typecom(typeextend):
    global companytype
    companytype = ".com"
    companylabel.config(text = companytype)

com = Button(master,text='.com',command=typecom(".com"))
com.place(relx=0.2, rely=0.4, anchor=E)

org = Button(master,text='.org',command=typecom(".org"))
org.place(relx=0.3, rely=0.4, anchor=E)

inc = Button(master,text='.inc',command=typecom(".inc"))
inc.place(relx=0.393, rely=0.4, anchor=E)

it = Button(master,text='.it',command=typecom(".it"))
it.place(relx=0.460, rely=0.4, anchor=E)

ca = Button(master,text='.ca',command=typecom(".ca"))
ca.place(relx=0.540, rely=0.4, anchor=E)

india = Button(master,text='.in',command=typecom(".in"))
india.place(relx=0.615, rely=0.4, anchor=E)

net = Button(master,text='.net',command=typecom(".net"))
net.place(relx=0.713, rely=0.4, anchor=E)

edu = Button(master,text='.edu',command=typecom(".edu"))
edu.place(relx=0.820, rely=0.4, anchor=E)

gov = Button(master,text='.gov',command=typecom(".gov"))
gov.place(relx=0.924, rely=0.4, anchor=E)

#----------------------------------Most used----------------------------------------
label = Label(master, text="Most used:")
label.place(relx=0.3, rely=0.6, anchor=E)

google = Button(master,text='Google Classroom',command=gfunc)
google.place(relx=0.55, rely=0.7, anchor=E)

leetcode = Button(master,text='Leetcode',command=lfunc)
leetcode.place(relx=0.75, rely=0.7, anchor=E)

manual = Button(master,text='Switch to manual',command=myfunc)
manual.place(relx=0.7, rely=0.8, anchor=E)

master.mainloop()