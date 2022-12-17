from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk


###########################Functions

def reset_password():
    if mailentry.get()=='':
        messagebox.showerror('error', 'Please enter the email address reset your password')
    else:
        con = pymysql.connect(host='localhost', user='root', password='mypass', database='register')
        cur = con.cursor()
        cur.execute('select * from client where email=%s', mailentry.get())
        row = cur.fetchone()
        if row==None:
            messagebox.showerror('Error', 'Please enter the valid Email Address')

        else:
            con.close()

            def change_password():
                if securityquesCombo.get() == 'Select' or answerEntry.get() == '' or newpassEntry.get() == '':
                    messagebox.showerror('error', 'All fields are required')
                else:
                    con = pymysql.connect(host='localhost', user='root', password='mypass', database='register')
                    cur = con.cursor()
                    cur.execute('select * from client where email=%s and question=%s and answer=%s', (mailentry.get(),
                                securityquesCombo.get(), answerEntry.get()))
                    row = cur.fetchone()
                    if row==None:
                        messagebox.showerror('error', 'Security Question or Answer is Incorrect', parent=nice)

                    else:
                        cur.execute('update client set password=%s where email=%s', (newpassEntry.get(), mailentry.get()
                                                                                     ))
                        con.commit()
                        con.close()
                        messagebox.showinfo('Success', 'Password is reset, please login with new password', parent=nice
                                             )
                        securityquesCombo.current(0)
                        answerEntry.delete(0, END)
                        newpassEntry.delete(0, END)
                        nice.destroy()


            nice = Toplevel()
            nice.title('Forget Password')
            nice.geometry('470x560+400+60')
            nice.config(bg='white')
            nice.focus_force()
            nice.grab_set()
            forgetLabel = Label(nice, text='Forget', font=('times new roman', 22, 'bold'), bg='white')
            forgetLabel.place(x=128, y=10)

            forgetpassLabel = Label(nice, text='Password', font=('times new roman', 22, 'bold'), bg='white', fg='green')
            forgetpassLabel.place(x=225, y=10)

            passwordimage = PhotoImage(file='pass.png')
            passImageLabel = Label(nice, image=passwordimage, bg='white')
            passImageLabel.place(x=170, y=70)

            securityqueslabel = Label(nice, text='Security Questions', font=('times in roman', 19, 'bold'), bg='white')
            securityqueslabel.place(x=60, y=220)

            securityquesCombo = ttk.Combobox(nice, font=('times in roman', 19), state='readonly', width=25)
            securityquesCombo['values'] = ('Select', 'Your First Pet Name?', 'Your Birth Place?', 'Your Best Friend Name?',
                                        'Your Favorite Sports?', 'Your Favorite Hobby?')
            securityquesCombo.place(x=60, y=260)
            securityquesCombo.current(0)

            answerlabel = Label(nice, text='Answer', font=('times new roman', 19, 'bold'), bg='white')
            answerlabel.place(x=60, y=310)
            answerEntry = Entry(nice, font=('times new roman', 19), bg='white', width=30)
            answerEntry.place(x=60, y=350)

            newpasslabel = Label(nice, text='New Password', font=('times new roman', 19, 'bold'), bg='white')
            newpasslabel.place(x=60, y=400)
            newpassEntry = Entry(nice, font=('times new roman', 19), bg='white', width=30)
            newpassEntry.place(x=60, y=440)

            changepassButton = Button(nice, text='Change Password', font=('arial', 17, 'bold'), bg='green', fg='white'
                                      , cursor='hand2', activebackground='green', activeforeground='white'
                                      , command=change_password)
            changepassButton.place(x=130, y=500)



            nice.mainloop()


def main_window():
    okay.destroy()
    import main

def signin():
    if mailentry.get()==''or passwordentry.get()=='':
       messagebox.showerror('error', 'All Fields Are Required')

    else:
        try:
         con = pymysql.Connect(host='localhost', user='root', password='mypass', database='register')
         cur = con.cursor()
         cur.execute('select * from client where email=%s and password=%s', (mailentry.get(), passwordentry.get()))
         row = cur.fetchone()

         if row==None:
             messagebox.showerror('error', 'Invalid Email or Password')
         else:
             messagebox.showinfo('success', 'welcome')
             okay.destroy()
             import restaurent
         con.close()
        except Exception as e:
            messagebox.showerror('error',f'Error is due to{e}')


#############GUI#############

okay = Tk()


okay.geometry('900x600+50+50')
okay.title('Login page')

bgloginimage = PhotoImage(file='loginbg.png')
bgloginLabel = Label(okay, image=bgloginimage)
bgloginLabel.place(x=0, y=0)

frame = Frame(okay, width=560, height=320, bg='white')
frame.place(x=180, y=140)

userimage = PhotoImage(file='user.png')
userimageLabel = Label(frame, image=userimage, bg='white')
userimageLabel.place(x=10, y=50)

passwordlabel = Label(frame, text='Password', font=('arial', 22, 'bold'), bg='white')
passwordlabel.place(x=220, y=120)
passwordentry = Entry(frame, font=('arial', 22), bg='white')
passwordentry.place(x=220, y=160)

regbutton = Button(frame, text='Register New Account?', font=('arial', 12), bd=0, bg='white', cursor='hand2'
                   , activebackground='white', command=main_window)
regbutton.place(x=220, y=200)

forgetbutton = Button(frame, text='forget password?', font=('arial', 12), bd=0, bg='white', cursor='hand2'
                      , activebackground='white', activeforeground='red', fg='red', command=reset_password)
forgetbutton.place(x=410, y=200)

loginbutton = Button(frame, text='Login', font=('arial', 18, ' bold'), fg='white', bg='gray20', cursor='hand2'
                     , activebackground='gray20', activeforeground='white', command=signin)
loginbutton.place(x=450, y=240)

maillabel = Label(frame, text='Email', font=('arial',22,'bold'), bg='white')
maillabel.place(x=220, y=32)
mailentry = Entry(frame, font=('arial', 22), bg='white')
mailentry.place(x=220, y=70)

okay.mainloop()


