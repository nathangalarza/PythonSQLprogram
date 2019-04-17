import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(user='root', password='Minicooper2010',
  host='127.0.0.1',database="company")
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SELECT FirstName, LastName FROM COMPANY.VISITORS")
counter = 0
window = Tk()
for x in mycursor:
  print(x)
  counter +=1  
  lbl = Label(window, text=x)
  window.title("My Server ")
  lbl.grid(column=0, row=counter)

window.mainloop()






