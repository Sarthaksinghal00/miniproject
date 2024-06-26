import  tkinter
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="7057",auth_plugin="mysql_native_password")
cur=con.cursor(buffered=True)


try:
    cur.execute("use registrations")
except:
    cur.execute("create database registrations")
    cur.execute("use registrations")

try:
    cur.execute("describe person")
except:
    cur.execute("create table person (id int primary key auto_increment, name varchar(50), gender varchar(30), email  varchar(30),mobileNo varchar(10))")


def Registrations():
    cur.execute(f"insert into person(name,gender,email,mobileNo) values('{e2.get()}','{e4.get()}','{e5.get()}','{e6.get()}')")
    con.commit()

    # //ram ram


win =tkinter.Tk()
win.geometry("500x500")
win.title("person registration portal")

# label

l1=tkinter.Label(win,text="Person Deatal")
l1.grid(row=1,column=1)
# e1=tkinter.Entry(win)
# e1.grid(row=1,column=2)

l2=tkinter.Label(win,text="Name")
l2.grid(row=2,column=1)
e2=tkinter.Entry(win)
e2.grid(row=2,column=2)

# l3=tkinter.Label(win,text="Age")
# l3.grid(row=3,column=1)
# e3=tkinter.Entry(win)
# e3.grid(row=3,column=2)

l4=tkinter.Label(win,text="Gender")
l4.grid(row=4,column=1)
e4=tkinter.Entry(win)
e4.grid(row=4,column=2)

l5=tkinter.Label(win,text="Email")
l5.grid(row=5,column=1)
e5=tkinter.Entry(win)
e5.grid(row=5,column=2)

l6=tkinter.Label(win,text="Mobile Number ")
l6.grid(row=6,column=1)
e6=tkinter.Entry(win)
e6.grid(row=6,column=2)
# button 

b=tkinter.Button(win,text="Submit Here",command=Registrations)
b.grid(row=7,column=1)





win.mainloop()
