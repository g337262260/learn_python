#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""requests"""

__author__ = 'Guowei'

import requests
import chardet
from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
        self.alertButton1 = Button(self, text='Hello')
        self.alertButton1.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

def load_get():
    r = requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})
    print('URL:',r.url)
    print('Header:',r.headers)
    print('StatusCode',r.status_code)
    print('Text:',r.text)
def get_json():
    r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from'
                     '%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
    print("Json:",r.json())
if __name__ == '__main__':
    app = Application()
    app.master.title('Hello world')
    app.mainloop()