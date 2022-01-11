# masih belum jadi mager mau pelajari lagi tunggu mood lah

from tkinter import *
from tkinter import font

root = Tk()
root.geometry("600x600")
root.title("Calculator")
e = Text(root,width=50, height=3, font=("Arial", 12) )
e.grid(row = 0, column=0, columnspan=5)

button1 = Button(root, text="1", padx= 35, pady=20, width = 5, command= lambda: tombol_angka(1), font=("Arial", 14)).grid(row = 1, column= 0)
button2 = Button(root, text="2", padx= 35, pady=20, width = 5, command= lambda: tombol_angka(2), font=("Arial", 14)).grid(row = 1, column= 1)
button3 = Button(root, text="3", padx= 35, pady=20, width = 5, command= lambda: tombol_angka(3), font=("Arial",14)).grid(row = 1, column= 2)
button4 = Button(root, text="4", padx= 35, pady=20, width = 5, command= lambda: tombol_angka(4), font=("Arial",14)).grid(row = 2, column= 0)
button5 = Button(root, text="5", padx= 35, pady=20, width = 5, command= lambda: tombol_angka(5), font=("Arial",14)).grid(row = 2, column= 1)
button6 = Button(root, text="6", padx= 35, pady=20, width = 5, command= lambda: tombol_angka(6), font=("Arial",14)).grid(row = 2, column= 2)
button7 = Button(root, text="7", padx= 35, pady=20, width = 5, command= lambda: tombol_angka(7), font=("Arial",14)).grid(row = 3, column= 0)
button8 = Button(root, text="8", padx= 35, pady=20, width = 5, command= lambda: tombol_angka(8), font=("Arial",14)).grid(row = 3, column= 1)
button9 = Button(root, text="9", padx= 35, pady=20, width = 5, command= lambda: tombol_angka(9), font=("Arial",14)).grid(row = 3, column= 2)
button0 = Button(root, text="0", padx= 35, pady=20, width = 5, command= lambda: tombol_angka(0), font=("Arial",14)).grid(row = 4, column= 1)
#Button 0-9
def tombol_angka(number):
    global calculation
    calculation += str(number)
    e.delete(1.0, "end")
    e.insert(1.0, calculation)
# #tombol delete
# def hapus():
#     e.delete(0, END)


def rumus():
    global calculation
    try:
        calculation = str(eval(calculation))
        e.delete(1.0, "end")
        e.insert(1.0, calculation)
    except:
        clear()
        e.insert(1.0, "error")
        pass


# # hasil dan delete
# def hasil():
#     sec_number = e.get()
#     e.insert(0,  int(sec_number))
#     e.delete(0, END)

# tombol C
def clear():
    global calculation
    calculation = ""
    e.delete(1.0,"end")



# delete = Button(root, text=" <--", padx=35, pady=20, command = tombol_angka, bg = "red",width = 5,font=("Arial", 14)).grid(column = 3, row = 1, columnspan= 2)
equals = Button(root, text="=", padx= 140, pady=20, width = 5,command= rumus, bg = "blue", font=("Arial", 14)).grid(column= 1, row= 5, columnspan=3)

kurang =Button(root, text="-", padx=35, pady=20,width = 5, command =lambda: tombol_angka(str("-")), bg = "red", font=("Arial", 14)).grid(column = 3, row = 3, columnspan= 2 )
kali = Button(root, text="*", padx=35, pady=20,width = 5, command =lambda: tombol_angka(str("*")), bg = "red", font=("Arial", 14)).grid(column = 3, row = 4, columnspan= 2 )
penambahan = Button(root, text="+", padx=35, pady=20, width = 5, command =lambda: tombol_angka(str("+")),bg = "red", font=("Arial", 14)).grid(column = 3, row = 2,columnspan= 2 )
bagi = Button(root, text="/", padx=35, pady=20, width = 5,command =lambda: tombol_angka(str("/")), bg = "red", font=("Arial", 14)).grid(column = 3, row = 5, columnspan= 2 )

buttonK_Kiri = Button(root, text="(", padx= 35, pady=20,width = 5,command= lambda: tombol_angka(str("(")), font=("Arial", 14)).grid(row = 4, column= 0)
buttonK_Kanan = Button(root, text=")", padx= 35, pady=20,width = 5, command= lambda: tombol_angka(str(")")), font=("Arial", 14)).grid(row = 4, column= 2)

buttonC = Button(root, text="C", padx= 35, pady=20, width = 5, font=("Arial", 14), command = clear).grid(row = 5, column= 0)

root.mainloop()

