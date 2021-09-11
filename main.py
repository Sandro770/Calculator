import tkinter as tk
from tkinter.constants import END
from tkinter.font import Font
from functools import partial

class App:
    def initRoot(self,root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x300")
        self.root.minsize(300,300)
        self.root.grid_rowconfigure([0,1],weight=1)
        self.root.grid_columnconfigure(0,weight=1)
    def returnPressed(self,event):
        rawInput = self.resEnt.get()
        for i in range(0,len(rawInput)):
            if(rawInput[i] == ','):
                rawInput[i] = '.'
        try:
            self.resText.set(str(eval(rawInput)))
        except:
            print("something done wrong")
    def initRes(self):
        self.resText = tk.StringVar()
        resEnt = tk.Entry(self.root,textvariable = self.resText,font = ("DejaVu Sans",20))
        self.resEnt = resEnt
        self.resEnt.grid(row=0,column=0,sticky="nwse")
        self.resEnt.bind('<Return>', self.returnPressed)
    def addChar(self, char):
        if(char == '='):
            self.returnPressed(None)
        else:
            self.resEnt.insert(END,char)
    def initBttns(self):
        frmBttns = tk.Frame(master=self.root)
        frmBttns.grid(row=1,column=0,sticky="nwse")
        operation = [['7','8','9','+'],
                     ['4','5','6','-'],
                     ['1','2','3','*'],
                     [',','0','=','/']
                    ];
        frmBttns.grid_rowconfigure(list(range(0,len(operation))),weight=1)
        frmBttns.grid_columnconfigure(list(range(0,len(operation[0]))),weight=1)
        for r in range(0,len(operation)):
            for c in range(0,len(operation[r])):
                act = partial(self.addChar,operation[r][c])
                btn = tk.Button(frmBttns,text=operation[r][c],width=3,height=2,command= act)
                btn.grid(row=r,column=c,sticky="nwse")
    def __init__(self, root):
        self.initRoot(root)
        self.initRes()
        self.initBttns()
root = tk.Tk() 
app = App(root)
app.root.mainloop()
