import datetime
from tkinter import *
from tkinter import scrolledtext
import os

import insert_into
import select

class App:
     def __init__(self,win):
          self.master = win
          self.t1 = Entry(width=30)
          self.t1.grid(column=1, row=1)
          self.t2 = Entry(width=30)
          self.t2.grid(column=1, row=2)
          self.t3 = Entry(width=30)
          self.t3.grid(column=1, row=3)

          self.lbl1 = Label(win, text='П.І.Б. відвідувача', justify=LEFT)
          self.lbl1.grid(column=0, row=1)
          self.lbl2 = Label(win, text='Хто дозволив', justify=LEFT)
          self.lbl2.grid(column=0, row=2)
          self.lbl3 = Label(win, text='Телефон', justify=LEFT)
          self.lbl3.grid(column=0, row=3)

          self.b1 = Button(win, text='Зберегти', command=self.add)
          self.b1.grid(column=0, row=4)
          self.b2 = Button(win, text='Друк', command=self.printer)
          self.b2.grid(column=1, row=4)
          self.b3 = Button(win, text='завантажити базу', command=self.select_dbase)
          self.b3.grid(column=1, row=5)
              

     def add(self):
          name1 = self.t1.get()
          name2 = self.t2.get()
          tel = self.t3.get()
          data_time = datetime.datetime.today().strftime('%Y-%m-%d %X')
          insert_into.ins_in([name1, name2, int(tel), data_time])
          self.t1.delete(0,END)
          self.t2.delete(0,END)
          self.t3.delete(0,END)

     def printer(self):
          s = self.show_db.curselection()
          s2 = self.show_db.get(s[0])
          print(s2)
          strig = 'Відвідувач: '+ str(s2[1])+'\nПрацівник: '+ str(s2[2])+ \
                '\nТелефон: '+ str(s2[3])+'\nДата візиту: '+ str(s2[4])
          f = open(r'12.txt', 'w')
          f.write(strig)
          f.close
          os.startfile(r'12.txt', 'print')
          

     def select_dbase(self):
          self.show_db = Listbox(width=50, selectbackground='gray')
          self.show_db.grid(column=1, row=7)
          insert_db_text = select.sel()
          for i in insert_db_text:
               self.show_db.insert(END, i)

              
                

window = Tk()
app = App(window)
window.title('Перепустка')
window.geometry("500x500+10+10")
window.mainloop()