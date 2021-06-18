import datetime
from tkinter import *
from tkinter import scrolledtext
import os

import insert_into
import select

class App:
     def __init__(self,win):
          self.master = win
          self.lbl1 = Label(win, text='П.І.Б. відвідувача')
          self.lbl2 = Label(win, text='Хто дозволив')
          self.lbl3 = Label(win, text='Телефон')

          self.t1 = Entry(bd=3)
          self.t2 = Entry()
          self.t3 = Entry()
          self.show_db = Listbox(width=50)
          


          self.lbl1.place(x=100, y=50)
          self.lbl2.place(x=100, y=100)
          self.lbl3.place(x=100, y=150)
          self.show_db.place(x=100, y=350)

          
          

          self.t1.place(x=200, y=50)
          self.t2.place(x=200, y=100)
          self.t3.place(x=200, y=150)

          self.b1 = Button(win, text='Зберегти', command=self.add)
          self.b2 = Button(win, text='Друк', command=self.printer)
          self.b3 = Button(win, text='завантажити базу', command=self.select_dbase)

          self.b1.place(x=100, y=250)
          self.b2.place(x=200, y=250)
          self.b3.place(x=300, y=250)
          
          

     def add(self):
          name1 = self.t1.get()
          name2 = self.t2.get()
          tel = int(self.t3.get())
          data_time = datetime.datetime.today().strftime('%Y-%m-%d %X')
          insert_into.ins_in([name1, name2, tel, data_time])

     def printer(self):
          os.startfile(r'C:\Users\admin\Desktop\python\проходная_пропуск\12.txt', 'print')

     def select_dbase(self):
          i = 0
          insert_db_text = select.sel()
          for i in insert_db_text:
               self.show_db.insert(0, i)  
          

window = Tk()
app = App(window)
window.title('Перепустка на Python')
window.geometry("500x600+10+10")
window.mainloop()
          
input()