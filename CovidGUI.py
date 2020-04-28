## Maj Myo Min Hein Python COVID 19 Analysis 
import json
import requests
import tkinter as Tkinter
from tkinter import ttk
import matplotlib.pyplot as plt
import math
 
 
global coun 
Form1 = Tkinter.Tk()
Form1.title("Maj MMH App")
Form1.geometry('350x200')

 
def callback(*args):
    global coun
    coun = combo.get()
    global Form1
    Form1.destroy()


lab = ttk.Label(Form1,text="Select")
lab.grid(column=0,row=0)
combo = ttk.Combobox(Form1)
country=[]
resp = requests.get('https://api.covid19api.com/countries')
 
if resp.status_code != 200:
              # This means something went wrong.
              raise ApiError('GET /tasks/ {}'.format(resp.status_code))
i =1
 
for todo_item in resp.json():
    i = i+1
    #print('{} {} {} {}'.format(todo_item['Confirmed'], todo_item['Deaths'], todo_item['Recovered'], todo_item['Date']))
    ck = todo_item['Country']
    country.insert(i,ck)

country.sort()               
combo['values']= country
combo.current(1) #set the selected item
combo.grid(column=2, row=0)
combo.bind("<<ComboboxSelected>>", callback)
 
btn = ttk.Button(Form1, text="Call Callback", command=callback);

Form1.mainloop()
 




#self.wm_iconbitmap("icon.ico")
textFont1 = ("Arial", 10, "bold italic")
textFont2 = ("Arial", 16, "bold")
textFont3 = ("Arial", 8, "bold")


 
class LabelWidget(Tkinter.Entry):
    def __init__(self, master, x, y, text):
        self.text = Tkinter.StringVar()
        self.text.set(text)
        


        Tkinter.Entry.__init__(self, master=master)
        self.config(relief="ridge", font=textFont1,
                    bg="#ffffff000", fg="#000000fff",
                    readonlybackground="#ffffff000",
                    justify='center',width=9,
                    textvariable=self.text,
                    state="readonly")
        self.grid(column=x, row=y)

class EntryWidget(Tkinter.Entry):
    def __init__(self, master, x, y):
        Tkinter.Entry.__init__(self, master=master)
        self.value = Tkinter.StringVar()
        self.config(textvariable=self.value, width=8,
                    relief="ridge", font=textFont1,
                    bg="#ddddddddd", fg="#000000000",
                    justify='center')
        self.grid(column=x, row=y)
        self.value.set("nn")

          
class EntryGrid(Tkinter.Tk):
    ''' Dialog box with Entry widgets arranged in columns and rows.'''
    def __init__(self, colList, rowList, title="U Myo(Stay Home) Covid 19 Analysis"):
        self.cols = colList[:]
        self.colList = colList[:]
        self.colList.insert(0, "")
        self.rowList = rowList
        Tkinter.Tk.__init__(self)
        self.title(title)
 
        self.mainFrame = Tkinter.Frame(self)
        self.mainFrame.config(padx='5.0m', pady='5.0m')
        self.mainFrame.grid()
        self.make_header()
 
        self.gridDict = {}
        for i in range(1, len(self.colList)):
            for j in range(len(self.rowList)):
                w = EntryWidget(self.mainFrame, i, j+1)
                self.gridDict[(i-1,j)] = w.value
                def handler(event, col=i-1, row=j):
                    return self.__entryhandler(col, row)
                w.bind(sequence="<FocusOut>", func=handler)
 
                 

        j=0
        for todo_item in resp.json():
               #print('{} {} {} {}'.format(todo_item['Confirmed'], todo_item['Deaths'], todo_item['Recovered'], todo_item['Date']))
               ck = todo_item['Confirmed']
               ckk = str(ck)
               
               if ckk !='0':
                    self.set(0,j,todo_item['Confirmed'])
                    self.set(1,j,todo_item['Deaths'])
                    self.set(2,j,todo_item['Recovered'])
      
                    self.update_idletasks()
                    j=j+1
 
                
        self.mainloop()
 
    def make_header(self):
        self.hdrDict = {}
        for i, label in enumerate(self.colList):
            def handler(event, col=i, row=0, text=label):
                return self.__headerhandler(col, row, text)
            w = LabelWidget(self.mainFrame, i, 0, label)
            self.hdrDict[(i,0)] = w
            w.bind(sequence="<KeyRelease>", func=handler)
 
        for i, label in enumerate(self.rowList):
            def handler(event, col=0, row=i+1, text=label):
                return self.__headerhandler(col, row, text)
            w = LabelWidget(self.mainFrame, 0, i+1, label[3])
             
            self.hdrDict[(0,i+1)] = w
            w.bind(sequence="<KeyRelease>", func=handler)
 
    def __entryhandler(self, col, row):
        s = self.gridDict[(col,row)].get()
        if s.upper().strip() == "EXIT":
            self.destroy()
        elif s.upper().strip() == "DEMO":
            self.demo()
        elif s.strip():
            print (s)
 
    def demo(self):
 
        for i in range(len(self.cols)):
            for j in range(len(self.rowList)):
                sleep(0.25)
                self.set(i,j,"sdsafsdfdf")
                self.update_idletasks()
                sleep(0.1)
                self.set(i,j,i+1+j)
                self.update_idletasks()

    def __headerhandler(self, col, row, text):
        ''' has no effect when Entry state=readonly '''
        self.hdrDict[(col,row)].text.set(text)
 
    def get(self, x, y):
        return self.gridDict[(x,y)].get()
 
    def set(self, x, y, v):
        self.gridDict[(x,y)].set(v)
        return v
 
if __name__ == "__main__":
     global coun
     print (coun)
     cols = [ 'Confirm', 'Death', 'Recovered']
     rows  = []
     resp = requests.get('https://api.covid19api.com/total/country/'+coun)
     #resp = requests.get('https://api.covid19api.com/live/country/Myanmar/status/confirmed')
     if resp.status_code != 200:
              # This means something went wrong.
              raise ApiError('GET /tasks/ {}'.format(resp.status_code))
     i =1
     rowConfirmed=[]
     exponentialGrouth=[]
 
     for todo_item in resp.json():
               ck = todo_item['Confirmed']
               ckk = str(ck)               
               if ckk !='0':
                   if i==30:
                       k = math.log1p(int(ckk))/30
                       print (ckk)
                       print (k)
                   i = i+1
     i=1    
     for todo_item in resp.json():
               row=[]
               #print('{} {} {} {}'.format(todo_item['Confirmed'], todo_item['Deaths'], todo_item['Recovered'], todo_item['Date']))
               ck = todo_item['Confirmed']
               ckk = str(ck)
               
               if ckk !='0': 
                    row.insert(0,todo_item['Confirmed'])
                    row.insert(1,todo_item['Deaths'])
                    row.insert(2,todo_item['Recovered'])
                    row.insert(3,todo_item['Date'])
                    rows.insert(i, row)
                    rowConfirmed.insert(i,todo_item['Confirmed'])
                    #X = 8*math.exp(i*0.16612022)
                    X = 1*math.exp(i*k)
                    exponentialGrouth.insert(i,X)
                    i = i+1
     
     app = EntryGrid(cols,rows,resp)
     print (exponentialGrouth)
 
  


 
         
     #print (exponentialGrouth)
     #plt.plot(exponentialGrouth,'g^')
     plt.plot(rowConfirmed,'r--')
     plt.title('COVID-19 '+coun+' Comparison between real cases and exponential growth \n ')
     plt.ylabel('COVID-19 Total Confirmed Cases')
     plt.xlabel('Times (previous days)')
     plt.text(3, 1220, 'Red dash line - Real Comfirmed \n Green Triangle - Exp Growth', style='italic',
        bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})
     plt.show()
     
     plt.plot(exponentialGrouth,'g^')
     plt.title('COVID-19 '+coun+' Comparison between real cases and exponential growth \n ')
     plt.ylabel('COVID-19 Total Confirmed Cases')
     plt.xlabel('Times (previous  days)')
     plt.text(3, 1220, 'Red dash line - Real Comfirmed \n Green Triangle - Exp Growth', style='italic',
        bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})
     plt.show()


