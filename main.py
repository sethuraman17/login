from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import pymysql




# functions



def login_window():
    root.destroy()
    import login



def clear():
    entryfirstname.delete(0, END)
    entrylastname.delete(0, END)
    entrycontact.delete(0, END)
    entryemail.delete(0, END)
    entrypassword.delete(0, END)
    entryconfirmpassword.delete(0, END)
    entryanswer.delete(0, END)
    comboxquestion.current(0)
    check.set(0)

def register():
    if entryfirstname.get() == '' or entryemail.get() == '' or entrycontact.get() == '' or entrylastname.get() == ''\
        or entrypassword.get() == '' or entryconfirmpassword.get() == '' or comboxquestion.get() == 'Select'\
        or entryanswer.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')

    elif entrypassword.get() != entryconfirmpassword.get():
        messagebox.showerror('Error', 'Password Mismatch')

    elif check.get() == 0:
        messagebox.showerror('Error', 'Please agree to our terms & conditions')

    else:
        try:
         con = pymysql.connect(host='localhost', user='root', password='mypass', database='register')
         cur = con.cursor()
         cur.execute('select * from client where email=%s', entryemail.get())
         row = cur.fetchone()
         if row!=None:
             messagebox.showerror('Error', 'User Already Exists')

         else:
             cur.execute(
                 'insert into client(f_name,l_name,contact,email,question,answer,password)values(%s,%s,%s,%s,%s,%s,%s)',
                         (entryfirstname.get(), entrylastname.get(), entrycontact.get(), entryemail.get(), comboxquestion.get(),
                          entryanswer.get(), entrypassword.get()))
             con.commit()
             con.close()

             messagebox.showinfo('Success', 'Registration is successfull')
             clear()
             root.destroy()
             import login

        except Exception as e:
            messagebox.showerror('error', f'Error due to {e}')





# GUI

root = Tk()

root.geometry('1350x710+10+10')
root.title('Registration Form')

bgimage = PhotoImage(file='bg.png')
bglabel = Label(root, image=bgimage)
bglabel.place(x=0, y=0)

mainFrame = Frame(root, width=625, height=600)
mainFrame.place(x=630, y=30)

titleLabel = Label(mainFrame, text='Registration Form', font=('arial', 22, 'bold'), fg='gold')
titleLabel.place(x=20, y=5)

firstnameLabel = Label(mainFrame, text='First Name', font=('times new roman', 18, 'bold'), fg='gray20')
firstnameLabel.place(x=20, y=80)
entryfirstname = Entry(mainFrame, font=('times new roman', 18), bg='lightgray')
entryfirstname.place(x=20, y=115)

lastnameLabel = Label(mainFrame, text='Last Name', font=('times new roman', 18, 'bold'), fg='gray20')
lastnameLabel.place(x=370, y=80)
entrylastname = Entry(mainFrame, font=('times new roman', 18), bg='lightgray')
entrylastname.place(x=370, y=115)

contactLabel = Label(mainFrame, text='Contact', font=('times new roman', 18, 'bold'), fg='gray20')
contactLabel.place(x=20, y=200)
entrycontact = Entry(mainFrame, font=('times new roman', 18), bg='lightgray')
entrycontact.place(x=20, y=235)

emailLabel = Label(mainFrame, text='Email ID', font=('times new roman', 18, 'bold'), fg='gray20')
emailLabel.place(x=370, y=200)
entryemail = Entry(mainFrame, font=('times new roman', 18), bg='lightgray')
entryemail.place(x=370, y=235)

questionLabel = Label(mainFrame, text='Security Question', font=('times new roman', 18, 'bold'), fg='gray20')
questionLabel.place(x=20, y=320)

comboxquestion = Combobox(mainFrame, font=('times new roman', 16), state='readonly')
comboxquestion['values'] = ('Select', 'Your First Pet Name?', 'Your Birth Place?', 'Your Best Friend Name?',
                            'Your Favorite Sports?', 'Your Favorite Hobby?')

comboxquestion.place(x=20, y=355)
comboxquestion.current(0)

answerLabel = Label(mainFrame, text='Answer', font=('times new roman', 18, 'bold'), fg='gray20')
answerLabel.place(x=370, y=320)
entryanswer = Entry(mainFrame, font=('times new roman', 18), bg='lightgray')
entryanswer.place(x=370, y=355)

passwordLabel = Label(mainFrame, text='Password', font=('times new roman', 18, 'bold'), fg='gray20')
passwordLabel.place(x=20, y=440)
entrypassword = Entry(mainFrame, font=('times new roman', 18), bg='lightgray', show='*')
entrypassword.place(x=20, y=475)

confirmpasswordLabel = Label(mainFrame, text='Confirm Password', font=('times new roman', 18, 'bold'), fg='gray20')
confirmpasswordLabel.place(x=370, y=440)
entryconfirmpassword = Entry(mainFrame, font=('times new roman', 18), bg='lightgray', show='*')
entryconfirmpassword.place(x=370, y=475)

check = IntVar()
checkbutton = Checkbutton(mainFrame, text='I Agree All The terms & conditions', onvalue=1, offvalue=0, variable=check,
                          font=('times new roman', 14, 'bold'))
checkbutton.place(x=20, y=530)

buttonimage = PhotoImage(file='button.png')
registorbutton = Button(mainFrame, image=buttonimage, bd=0, cursor='hand2', command=register)
registorbutton.place(x=250, y=563)

loginimage = PhotoImage(file='login.png')
loginbutton = Button(root, image=loginimage, bd=0, bg='gold', cursor='hand2', command=login_window)
loginbutton.place(x=240, y=330)


root.mainloop()
