# -*- coding: utf-8 -*-
'''
Created on 2017年12月16日

@author: tony
'''

from Tkinter import Frame, Button, Entry
import tkMessageBox

class Application(Frame):
    
    def __init__(self, master = None):
        
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        
        #self.helloLabel = Label(self, text = 'Hello, world!')
        #self.helloLabel.pack()
        #self.quitButton = Button(self, text = 'Quit', command = self.quit)
        #self.quitButton.pack()
        
        self.nameInput = Entry(self)
        self.nameInput.pack()
        
        self.alterButton = Button(self, text = 'Hello', command = self.hello)
        self.alterButton.pack()
        
    def hello(self):
        
        name = self.nameInput.get() or ' world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)
        
app = Application()
app.master.title('Hello World')
app.mainloop()