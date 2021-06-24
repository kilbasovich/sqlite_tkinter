import datetime
import os
from tkinter import *
from tkinter import ttk
import insert_into
import select

class App:
     def __init__(self,win):
          self.master = win
          self.t1 = Entry(width=40)
          self.t1.grid(column=1, row=1)
          self.t2 = Entry(width=40)
          self.t2.grid(column=1, row=2)
          self.t3 = Entry(width=40)
          self.t3.grid(column=1, row=3)
          
          self.lbl0 = Label(win, text='---', justify=LEFT)
          self.lbl0.grid(column=1, row=0)
          self.lbl1 = Label(win, text='П.І.Б. відвідувача:',width=30, justify=LEFT)
          self.lbl1.grid(column=0, row=1)
          self.lbl2 = Label(win, text='Хто дозволив:',width=30, justify=LEFT)
          self.lbl2.grid(column=0, row=2)
          self.lbl3 = Label(win, text='Кабінет:',width=30, justify=LEFT)
          self.lbl3.grid(column=0, row=3)

          self.b1 = Button(win, text='Зберегти', width=30, command=self.add)
          self.b1.grid(column=1, row=4)
          self.b2 = Button(win, text='Друк', width=30, command=self.printer)
          self.b2.grid(column=1, row=5)
          self.b3 = Button(win, text='Завантажити дані з бази', width=30, command=self.select_dbase)
          self.b3.grid(column=1, row=6)
          
          self.tv = ttk.Treeview(win, columns=(1,2,3,4,5), show='headings')
          self.tv.grid(column=0, row=9)
          self.tv.heading(1, text='id',)
          self.tv.heading(2, text='Відвідувач')
          self.tv.heading(3, text='Працівник')
          self.tv.heading(4, text='Кабінет')
          self.tv.heading(5, text='Дата візиту')


     def add(self):
          name1 = self.t1.get()
          name2 = self.t2.get()
          cabinet = self.t3.get()
          data_time = datetime.datetime.today().strftime('%Y-%m-%d %X')
          insert_into.ins_in([name1, name2, int(cabinet), data_time])
          self.t1.delete(0,END)
          self.t2.delete(0,END)
          self.t3.delete(0,END)

     def printer(self):
          s = self.tv.selection()
          s2 = self.tv.item(s)
          print(s2['values'])
          strig = '   ПЕРЕПУСТКА\nВідвідувач: '+ str(s2['values'][1])+'\nПрацівник: '+ str(s2['values'][2])+ \
                '\nКабінет: '+ str(s2['values'][3])+'\nДата візиту: '+ str(s2['values'][4])
          f = open(r'12.txt', 'w')
          f.write(strig)
          f.close
          os.startfile(r'12.txt', 'print')
          

     def select_dbase(self):
          insert_db_text = select.sel()
          for i in insert_db_text:
               self.tv.insert('','end', values=i)


window = Tk()
app = App(window)
window.title('Перепустка')
window.geometry("500x500+10+10")
window.mainloop()