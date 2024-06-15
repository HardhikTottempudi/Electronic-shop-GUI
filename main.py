from tkinter import *
from tkinter import font
import tkinter as tk
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
import smtplib
import time
import datetime

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="hardhik4488",
  database="12b_hardhik"
)

cu = db.cursor()

#Creating the main window
wn = Tk()
wn.title("Project")
wn.configure(bg='grey')
wn.minsize(width=500,height=500)
wn.geometry("700x600")
headingFrame1 = Frame(wn,bg="black",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to Render electronics \n Shop", fg='grey19', font=('Courier',15,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

cu.execute('create table if not exists bill(Item_type varchar(20),Item_name varchar(50),Price int(20))')
offer = 0
cu.execute("create table if not exists bill_final(sl_no int,Item_type varchar(20),Item_name varchar(50),Price int(20))")
def sign_in():
  wn6 = tk.Tk()
  wn6.title('Login')
  wn6.geometry("500x300")

  wn6.configure(bg='Lightblue1')
  headingframe_login = tk.Frame(wn6, bg="black", bd=5)
  headingframe_login.place(x=170, y=60, relwidth=0.4, relheight=0.14)

  headingLabel_login = tk.Label(headingframe_login, text="LOGIN & SIGN UP", fg='grey19', font=('Courier', 15, 'bold'))
  headingLabel_login.place(relx=0, rely=0, relwidth=1, relheight=1)


  def signin_f():
    wn10 = Tk()
    wn10.title('Login')
    wn10.geometry("270x110")

    user_l = Label(wn10, text= 'Username')
    user_l.place(x=25,y=25)
    user_e = Entry(wn10)
    user_e.place(x=100,y=25)

    pass_l = Label(wn10, text='Password')
    pass_l.place(x=25, y=50)
    pass_e = Entry(wn10,show='*')
    pass_e.place(x=100, y=50)

    def signin():
      user = user_e.get()
      password = pass_e.get()

      cu.execute('select * from login_data')
      data_login = list(cu.fetchall())
      print(data_login)
      global offer
      offer = 0

      for i in range(len(data_login)):
        if data_login[i][0] == user and data_login[i][1] == str(password):
            offer = 0.15

      if offer == 0.15:
        messagebox.showinfo('Login successful','You can get 15% offer')
        wn10.destroy()
        wn6.destroy()
      else:
        messagebox.showinfo('Warning','Wrong password')
        wn10.destroy()
        wn6.destroy()


    login_e = Button(wn10, text='Enter',command=signin)
    login_e.place(x=200,y=75)


    wn10.mainloop()


  def signup_f():
    wn11 = Tk()
    wn11.title('Sign up')
    wn11.geometry("300x125")

    user_l_up= Label(wn11, text='Username to create account')
    user_l_up.place(x=25, y=25)
    user_e_up = Entry(wn11)
    user_e_up.place(x=150, y=25)

    pass_l_up = Label(wn11, text='Enter Password')
    pass_l_up.place(x=25, y=50)
    pass_e_up = Entry(wn11,show='*')
    pass_e_up.place(x=150, y=50)

    confirming_pass = Label(wn11, text='Re-enter Password')
    confirming_pass.place(x=25, y=75)
    confirming_pass_e = Entry(wn11,show='*')
    confirming_pass_e.place(x=150, y=75)


    def create_acc():
      if pass_e_up.get() == confirming_pass_e.get():
        a=user_e_up.get()
        b=pass_e_up.get()
        sql = "INSERT INTO login_data (Username, password) VALUES (%s, %s)"
        val = (a,b)
        cu.execute(sql, val)
        db.commit()
        messagebox.showinfo('details','Details Updated')
        time.sleep(1)
        wn11.destroy()
        wn6.destroy()


    b = Button(wn11, text='Enter',command=create_acc).place(x=200,y=100)
    wn11.mainloop()



  signin_b = tk.Button(wn6, text='Sign in',height=2,width=10,command=signin_f)
  signin_b.place(x=170,y=150)
  signup_b = tk.Button(wn6, text='Sign Up',height=2,width=10,command=signup_f)
  signup_b.place(x=270, y=150)


  wn6.mainloop()
global j
j=0

def delProd():
  global j
  wn7 = Tk()
  wn7.title('Delete products')
  wn7.geometry("850x350")
  wn7.resizable(False,False)
  wn7.configure(bg='Light green')

  headingframe_del = Frame(wn7, bg="black", bd=5)
  headingframe_del.place(x=220, y=40, relwidth=0.4, relheight=0.14)

  headingLabel_del = Label(headingframe_del, text="DElETE PRODUCT", fg='grey19', font=('Courier', 15, 'bold'))
  headingLabel_del.place(relx=0, rely=0, relwidth=1, relheight=1)

  cu.execute('SELECT * FROM bill')
  data_bill = cu.fetchall()
  if len(data_bill) >= 1 and j == 0:
    sl_no = []

    for i in range(len(data_bill)):
      sl_no.append(i)
      com = 'insert into bill_final (sl_no,Item_type,Item_name,Price) values(%s,%s,%s,%s)'
      com_val = (i,) + data_bill[i]
      print(com_val)
      cu.execute(com, com_val)
      db.commit()
      j += 1

  cu.execute('SELECT * FROM bill_final')
  data_billfinal = cu.fetchall()

  tv4 = ttk.Treeview(
    wn7,
    columns=(1, 2, 3, 4),
    show='headings',
    height=5
  )
  tv4.place(x=30, y=100)

  tv4.heading(1, text='Sl NO')
  tv4.heading(2, text='Item type')
  tv4.heading(3, text='Item Name')
  tv4.heading(4, text='Price')
  h4 = 0
  for i in data_billfinal:
    tv4.insert(parent='', index=h4, iid=h4, values=i)
    h4 += 1

  style = ttk.Style()
  style.theme_use("default")
  style.map("Treeview")


  def del_item():
    del_sl = del_e1.get()
    query = 'DELETE FROM bill_final WHERE sl_no = '+del_sl
    cu.execute(query)
    db.commit()
    tv4.delete(del_sl)
    del_e1.delete(0, END)
    del_e1.insert(0, '')

  del_l = Label(wn7, text='Select record to Delete from the bill: ',bg='medium turquoise')
  del_l.place(x=130,y=250)
  del_e1 = Entry(wn7)
  del_e1.place(x=350,y=250)
  del_b = Button(wn7, text='Enter',command=del_item)
  del_b.place(x=480,y=250)
  wn7.mainloop()

def bill():
  wn8 = Tk()
  wn8.title('Bill')
  wn8.geometry("880x400")
  wn8.configure(bg='maroon3')
  global j
  headingframe_bill = Frame(wn8, bg="black",bd=5)
  headingframe_bill.place(x=200,y=60,relwidth=0.4, relheight=0.14)

  headingLabel_bill = Label(headingframe_bill, text="BIll", fg='grey19',font=('Courier', 15, 'bold'))
  headingLabel_bill.place(relx=0, rely=0, relwidth=1, relheight=1)

  cu.execute('SELECT * FROM bill')
  data_bill = cu.fetchall()
  if len(data_bill) >= 1 and j == 0:
    sl_no = []

    for i in range(len(data_bill)):
      sl_no.append(i)
      com = 'insert into bill_final (sl_no,Item_type,Item_name,Price) values(%s,%s,%s,%s)'
      com_val = (i,) + data_bill[i]
      print(com_val)
      cu.execute(com, com_val)
      db.commit()
      j += 1

  cu.execute('SELECT * FROM bill_final')
  data_bill = cu.fetchall()

  tv5 = ttk.Treeview(
    wn8,
    columns=(1, 2, 3, 4),
    show='headings',
    height=5
  )
  tv5.place(x=60, y=140)

  tv5.heading(1, text='SL NO')
  tv5.heading(2, text='Item type')
  tv5.heading(3, text='Item Name')
  tv5.heading(4, text='Price')
  h5 = 0
  for i in data_bill:
    tv5.insert(parent='', index=h5, iid=h5, values=i)
    h5 += 1

  style = ttk.Style()
  style.theme_use("default")
  style.map("Treeview")

  bill_info = Frame(wn8,bg="white",bd=5)
  bill_info.place(x=60,y=270,relwidth=0.7, relheight=0.18)

  tot_am = Label(bill_info,text='Amount: ',bg='white',fg='grey19',font=('Courier', 8, 'bold'))
  tot_am.place(x=5,y=3)
  tot_price=[]
  for i in data_bill:
    tot_price.append(i[3])
  tot_price1 = sum(tot_price)
  print(type(tot_price1))
  tot_am1 = Label(bill_info,text=tot_price1,bg='white',fg='grey19',font=('Courier', 8, 'bold'))
  tot_am1.place(x=65,y=3)
  print(offer)

  if offer == 0.15:
    tot1 = Label(bill_info,text='Total amount:',bg='white',fg='grey19',font=('Courier', 8, 'bold'))
    tot1.place(x=5,y=35)

    tot1_l = Label(bill_info,text=1.05*((1-offer)*tot_price1),bg='white',fg='grey19',font=('Courier', 8, 'bold'))
    tot1_l.place(x=100,y=37)
  else:
    tot12 = Label(bill_info, text='Total amount:', bg='white', fg='grey19', font=('Courier', 8, 'bold'))
    tot12.place(x=5, y=37)

    tot12_l = Label(bill_info,text=1.05*(tot_price1),bg='white', fg='grey19', font=('Courier', 8, 'bold'))
    tot12_l.place(x=100, y=37)

  vat = Label(bill_info, text='VAT: ', bg='white', fg='grey19', font=('Courier', 8, 'bold'))
  vat.place(x=5, y=20)
  vat1 = Label(bill_info, text='5% of the total amount ', bg='white', fg='grey19', font=('Courier', 8, 'bold'))
  vat1.place(x=55, y=20)
  mail = Label(bill_info, text='Enter Email ID: ', bg='white', fg='grey19', font=('Courier', 8, 'bold'))
  mail.place(x=360, y=10)
  mail_e = Entry(bill_info, bg='light cyan', borderwidth= 4, width=30)
  mail_e.place(x=370,y=30)

  def purchase():
    try:
      message1 = ''
      for i in data_bill:
        message1 += str(i) + '\n' + '\n'
      message2 = """Thank you,
      Render electronics"""
      message = """
      Subject: Render delivery                                                                       {date}

      Thank you for choosing Render electronics.The products will be deliverd in 4-5 buisness days
      Bill:

      {message1}
      {message2}

            """.format(date=datetime.date.today(), message1=message1, message2=message2)
      server = smtplib.SMTP("smtp.gmail.com", 587)
      server.starttls()
      server.login('thardhiktiger2@gmail.com', 'yazvoelhqlkkigoh')
      server.sendmail('thardhiktiger2@gmail.com', mail_e.get(), message)
      messagebox.showinfo("Bill", 'Purchase successful')
      time.sleep(1)
      wn.destroy()
      wn8.destroy()

    except Exception as e:
        print(e)
    cu.execute('drop table bill')
    cu.execute('drop table bill_final')
    db.commit()

  purchase_b = Button(bill_info, text='PURCHASE ',pady=7 ,padx=7,bg='maroon', fg='white', font=('Courier', 8, 'bold'),command=purchase)
  purchase_b.place(x=250,y=20)


  wn8.mainloop()


def viewProds():
  wn1 = Tk()
  wn1.title('View products')
  wn1.geometry("500x470")
  wn1.configure(bg='goldenrod')

  def smartphones_sql():
    wn2 = Tk()
    wn2.geometry("800x300")
    wn2.configure(bg='medium turquoise')
    headingframe_phones = Frame(wn2, bg="black", bd=5)
    headingframe_phones.place(x=200, y=50, relwidth=0.4, relheight=0.14)

    headingLabel_phones = Label(headingframe_phones, text="SMARTPHONES", fg='grey19', font=('Courier', 15, 'bold'))
    headingLabel_phones.place(relx=0, rely=0, relwidth=1, relheight=1)
    cu.execute('SELECT * FROM smartphones')
    data = cu.fetchall()

    tv = ttk.Treeview(
      wn2,
      columns=(1, 2, 3),
      show='headings',
      height=5
    )
    tv.place(x=60,y=100)

    tv.heading(1, text='Item type')
    tv.heading(2, text='Brand Name')
    tv.heading(3, text='Price')
    h = 0
    for i in data:
      tv.insert(parent='', index=h, iid=h, values=i)
      h += 1

    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")



    def add1_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()


      sql1 = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val1 = data[0]                      #('MOBILE','Iphone 13 mini',3000)

      cu.execute(sql1, val1)
      db.commit()



      #cu.execute('insert into bill values("%s","%s",%s)'%("MOBILE","Iphone 13 mini",3000))

    def add2_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql2 = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val2 = data[1]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql2, val2)
      db.commit()

    def add3_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql3 = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val3 = data[2]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql3, val3)
      db.commit()

    def add4_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql4 = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val4 = data[3]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql4, val4)
      db.commit()

    def add5_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql5 = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val5 = data[4]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql5, val5)
      db.commit()

    add1 = Button(wn2,text='Add',padx=20,pady=0.1,command=add1_f)
    add1.place(x=663,y=110)

    add2 = Button(wn2, text='Add',padx=20,pady=0.1,command=add2_f)
    add2.place(x=663, y=135)

    add3 = Button(wn2, text='Add',padx=20,pady=0.1,command=add3_f)
    add3.place(x=663, y=160)

    add4 = Button(wn2, text='Add',padx=20,pady=0.1,command=add4_f)
    add4.place(x=663, y=185)

    add5 = Button(wn2, text='Add',padx=20,pady=0.1,command=add5_f)
    add5.place(x=663, y=210)


    wn2.mainloop()


  def laptops_sql():
    wn3 = Tk()
    wn3.geometry("800x300")
    wn3.configure(bg='medium turquoise')
    headingframe_lap = Frame(wn3, bg="black", bd=5)
    headingframe_lap.place(x=200, y=50, relwidth=0.4, relheight=0.14)

    headingLabel_lap = Label(headingframe_lap, text="LAPTOPS", fg='grey19', font=('Courier', 15, 'bold'))
    headingLabel_lap.place(relx=0, rely=0, relwidth=1, relheight=1)
    cu.execute('SELECT * FROM laptops')
    data_laptops = cu.fetchall()

    tv1 = ttk.Treeview(
      wn3,
      columns=(1, 2, 3),
      show='headings',
      height=5
    )
    tv1.place(x=60,y=100)

    tv1.heading(1, text='Item type')
    tv1.heading(2, text='Brand Name')
    tv1.heading(3, text='Price')
    h1 = 0
    for i in data_laptops:
      tv1.insert(parent='', index=h1, iid=h1, values=i)
      h1 += 1

    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")

    def add1_lap_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql1_lap = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val1_lap = data_laptops[0]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql1_lap, val1_lap)
      cu.execute(sql1_lap, val1_lap)
      db.commit()

      #cu.execute('insert into bill values("%s","%s",%s)'%("MOBILE","Iphone 13 mini",3000))

    def add2_lap_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql2_lap = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val2_lap = data_laptops[1]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql2_lap, val2_lap)
      db.commit()

    def add3_lap_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql3_lap = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val3_lap = data_laptops[2]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql3_lap, val3_lap)
      db.commit()

    def add4_lap_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql4_lap = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val4_lap = data_laptops[3]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql4_lap, val4_lap)
      db.commit()

    def add5_lap_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql5_lap = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val5_lap = data_laptops[4]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql5_lap, val5_lap)
      db.commit()

    add1_lap= Button(wn3,text='Add',padx=20,pady=0.1,command=add1_lap_f)
    add1_lap.place(x=663,y=110)

    add2_lap = Button(wn3, text='Add',padx=20,pady=0.1,command=add2_lap_f)
    add2_lap.place(x=663, y=135)

    add3_lap = Button(wn3, text='Add',padx=20,pady=0.1,command=add3_lap_f)
    add3_lap.place(x=663, y=160)

    add4_lap = Button(wn3, text='Add',padx=20,pady=0.1,command=add4_lap_f)
    add4_lap.place(x=663, y=185)

    add5_lap = Button(wn3, text='Add',padx=20,pady=0.1,command=add5_lap_f)
    add5_lap.place(x=663, y=210)


    wn3.mainloop()


  def videogames_sql():
    wn4 = Tk()
    wn4.geometry("800x300")
    wn4.configure(bg='medium turquoise')
    headingframe_game = Frame(wn4, bg="black", bd=5)
    headingframe_game.place(x=200, y=50, relwidth=0.4, relheight=0.14)

    headingLabel_game = Label(headingframe_game, text="VIDEO GAMES", fg='grey19', font=('Courier', 15, 'bold'))
    headingLabel_game.place(relx=0, rely=0, relwidth=1, relheight=1)
    cu.execute('SELECT * FROM videogames')
    data_videogames = cu.fetchall()

    tv2 = ttk.Treeview(
      wn4,
      columns=(1, 2, 3),
      show='headings',
      height=5
    )
    tv2.place(x=60,y=100)

    tv2.heading(1, text='Item type')
    tv2.heading(2, text='Brand Name')
    tv2.heading(3, text='Price')
    h2 = 0
    for i in data_videogames:
      tv2.insert(parent='', index=h2, iid=h2, values=i)
      h2 += 1

    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")

    def add1_vd_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql1_videogames = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val1_videogames = data_videogames[0]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql1_videogames, val1_videogames)
      db.commit()

      #cu.execute('insert into bill values("%s","%s",%s)'%("MOBILE","Iphone 13 mini",3000))

    def add2_vd_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql2_videogames = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val2_videogames = data_videogames[1]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql2_videogames, val2_videogames)
      db.commit()

    def add3_vd_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql3_videogames = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val3_videogames = data_videogames[2]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql3_videogames, val3_videogames)
      db.commit()

    def add4_vd_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql4_videogames = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val4_videogames = data_videogames[3]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql4_videogames, val4_videogames)
      db.commit()

    def add5_vd_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql5_videogames = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val5_videogames = data_videogames[4]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql5_videogames, val5_videogames)
      db.commit()

    add1 = Button(wn4,text='Add',padx=20,pady=0.1,command=add1_vd_f)
    add1.place(x=663,y=110)

    add2 = Button(wn4, text='Add',padx=20,pady=0.1,command=add2_vd_f)
    add2.place(x=663, y=135)

    add3 = Button(wn4, text='Add',padx=20,pady=0.1,command=add3_vd_f)
    add3.place(x=663, y=160)

    add4 = Button(wn4, text='Add',padx=20,pady=0.1,command=add4_vd_f)
    add4.place(x=663, y=185)

    add5 = Button(wn4, text='Add',padx=20,pady=0.1,command=add5_vd_f)
    add5.place(x=663, y=210)


    wn4.mainloop()



  def tvaudio_sql():
    wn5 = Tk()
    wn5.geometry("800x300")
    wn5.configure(bg='medium turquoise')
    headingframe_audio = Frame(wn5, bg="black", bd=5)
    headingframe_audio.place(x=200, y=50, relwidth=0.4, relheight=0.14)

    headingLabel_audio = Label(headingframe_audio, text="TV & AUDIO", fg='grey19', font=('Courier', 15, 'bold'))
    headingLabel_audio.place(relx=0, rely=0, relwidth=1, relheight=1)
    cu.execute('SELECT * FROM tvaudio')
    data_tvaudio = cu.fetchall()

    tv3 = ttk.Treeview(
      wn5,
      columns=(1, 2, 3),
      show='headings',
      height=5
    )
    tv3.place(x=60,y=100)

    tv3.heading(1, text='Item type')
    tv3.heading(2, text='Brand Name')
    tv3.heading(3, text='Price')
    h3 = 0
    for i in data_tvaudio:
      tv3.insert(parent='', index=h3, iid=h3, values=i)
      h3 += 1

    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")

    def add1_tvaudio_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql1_tvaudio = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val1_tvaudio = data_tvaudio[0]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql1_tvaudio, val1_tvaudio)
      db.commit()

      #cu.execute('insert into bill values("%s","%s",%s)'%("MOBILE","Iphone 13 mini",3000))

    def add2_tvaudio_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql2_tvaudio = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val2_tvaudio = data_tvaudio[1]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql2_tvaudio, val2_tvaudio)
      db.commit()

    def add3_tvaudio_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql3_tvaudio = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val3_tvaudio = data_tvaudio[2]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql3_tvaudio, val3_tvaudio)
      db.commit()

    def add4_tvaudio_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql4_tvaudio = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val4_tvaudio = data_tvaudio[3]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql4_tvaudio, val4_tvaudio)
      db.commit()

    def add5_tvaudio_f():
      #cu.execute('select *  from smartphones')
      #data1 = cu.fetchall()

      sql5_tvaudio = "INSERT INTO bill (Item_type, Item_name, Price) VALUES (%s, %s, %s)"
      val5_tvaudio = data_tvaudio[4]                           #('MOBILE','Iphone 13 mini',3000)
      cu.execute(sql5_tvaudio, val5_tvaudio)
      db.commit()

    add1 = Button(wn5,text='Add',padx=20,pady=0.1,command=add1_tvaudio_f)
    add1.place(x=663,y=110)

    add2 = Button(wn5, text='Add',padx=20,pady=0.1,command=add2_tvaudio_f)
    add2.place(x=663, y=135)

    add3 = Button(wn5, text='Add',padx=20,pady=0.1,command=add3_tvaudio_f)
    add3.place(x=663, y=160)

    add4 = Button(wn5, text='Add',padx=20,pady=0.1,command=add4_tvaudio_f)
    add4.place(x=663, y=185)

    add5 = Button(wn5, text='Add',padx=20,pady=0.1,command=add5_tvaudio_f)
    add5.place(x=663, y=210)


    wn5.mainloop()


  #Button Placement
  # See smartPhones
  btn_smartphones = Button(wn1, text="SMARTPHONES", bg='Lightcyan2', fg='black', width=15, height=2,command=smartphones_sql)
  btn_smartphones['font'] = font.Font(size=11)
  btn_smartphones.place(x=160, y=100)

  btn_tvaudio = Button(wn1, text="TV & AUDIO", bg='Lightcyan2', fg='black', width=15, height=2,command=tvaudio_sql)
  btn_tvaudio['font'] = font.Font(size=11)
  btn_tvaudio.place(x=160, y=190)

  btn_laptops = Button(wn1, text="LAPTOPS", bg='Lightcyan2', fg='black', width=15, height=2,command=laptops_sql)
  btn_laptops['font'] = font.Font(size=11)
  btn_laptops.place(x=160, y=280)

  btn_videogame = Button(wn1, text="VIDEO GAMES", bg='Lightcyan2', fg='black', width=15, height=2,command=videogames_sql)
  btn_videogame['font'] = font.Font(size=11)
  btn_videogame.place(x=160, y=360)

  wn1.mainloop()

#Button to add a new product
btn1 = Button(wn,text="Sign in",bg='Lightblue1', fg='black', width=20,height=2,command=sign_in)
btn1['font'] = font.Font( size=12)
btn1.place(x=270,y=175)

#Button to delete a product
btn2 = Button(wn,text="Delete items",bg='Light green', fg='black',width=20,height=2,command=delProd)
btn2['font'] = font.Font( size=12)
btn2.place(x=270,y=255)

#Button to view all products
btn3 = Button(wn,text="View Products",bg='gold', fg='black',width=20,height=2,command= viewProds)
btn3['font'] = font.Font( size=12)
btn3.place(x=270,y=335)

#Button to add a new sale and generate bill
btn4 = Button(wn,text="Bill",bg='maroon3', fg='black', width=20,height=2,command = bill)
btn4['font'] = font.Font( size=12)
btn4.place(x=270,y=415)

wn.mainloop()
