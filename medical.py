import random
import time
from tkinter import *
from tkinter import filedialog, messagebox
import requests


# Functions


def reset():
    textreciept.delete(1.0, END)
    e_bandage.set('0')
    e_dettol.set('0')
    e_sticky_tape.set('0')
    e_thermometer.set('0')
    e_tweezers.set('0')
    e_spray.set('0')
    e_diapers.set('0')
    e_condom.set('0')
    e_cotton.set('0')
    e_cofsils.set('0')
    e_benadryl.set('0')
    e_haldi_kuf.set('0')
    e_d_15.set('0')
    e_babuline.set('0')
    e_ccf.set('0')
    e_tusq.set('0')
    e_kofnil.set('0')
    e_codral.set('0')
    e_mucinex_d.set('0')
    e_total.set('0')
    e_afrin.set('0')
    e_sudafed.set('0')
    e_dolo_650.set('0')
    e_paracetamol.set('0')
    e_codeine.set('0')
    e_robafen.set('0')
    e_hytuss.set('0')



    textbandage.config(state=DISABLED)
    textdettol.config(state=DISABLED)
    textsticky_tape.config(state=DISABLED)
    textthermometer.config(state=DISABLED)
    texttweezers.config(state=DISABLED)
    textspray.config(state=DISABLED)
    textdiapers.config(state=DISABLED)
    textcondom.config(state=DISABLED)
    textcotton.config(state=DISABLED)
    textcofsils.config(state=DISABLED)
    textbenadryl.config(state=DISABLED)
    texthaldi_kuf.config(state=DISABLED)
    textd_15.config(state=DISABLED)
    textbabuline.config(state=DISABLED)
    textccf.config(state=DISABLED)
    texttusq.config(state=DISABLED)
    textkofnil.config(state=DISABLED)
    textcodral.config(state=DISABLED)
    textmucinex_d.config(state=DISABLED)
    texttotal.config(state=DISABLED)
    textafrin.config(state=DISABLED)
    textsudafed.config(state=DISABLED)
    textdolo_650.config(state=DISABLED)
    textparacetamol.config(state=DISABLED)
    textcodeine.config(state=DISABLED)
    textrobafen.config(state=DISABLED)
    texthytuss.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)


    costoffirst_aidvar.set('')
    costofsyrupsvar.set('')
    costofpillsvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')


def send():
    if textreciept.get(1.0, END)=='\n':
        pass
    else:
        def send_msg():
            message = textarea.get(1.0, END)
            number = numberfield.get()
            auth = 'wjxfQIOcoyiJKC5DZeH0zTP8Ev2WBUY1hL7SNMG9lq4nF6tRukSIy8WhYLwk37rQ614DvEfaObFNuqsp'
            url = 'https://www.fast2sms.com/dev/bulkV2'

            params = {
                'authorization': auth,
                'message': message,
                'numbers': number,
                'sender-id': 'FSTSMS',
                'route': 'p',
                'language': 'english'
            }
            response = requests.get(url, params=params)
            dic = response.json()
            result = dic.get('return')
            if result == True:
                messagebox.showinfo('Send Successfully', 'Message Sent Successfully')

            else:
                messagebox.showerror('Error', 'Something went wrong')

        root2 = Toplevel()

        root2.title('SEND BILL')
        root2.config(bg='red4')
        root2.geometry('485x620+50+50')

        logoimage = PhotoImage(file='search.png')
        label = Label(root2, image=logoimage)
        label.pack(pady=5)

        numberlabel = Label(root2, text='Mobile Number', font=('arial', 18, 'bold', 'underline'), bg='red4', fg='white')
        numberlabel.pack(pady=5)

        numberfield = Entry(root2, font=('helvetica', 22, 'bold'), bd=3, width=24)
        numberfield.pack(pady=5)

        billlabel = Label(root2, text='BILL DETAILS', font=('arial', 18, 'bold', 'underline'), bg='red4', fg='white')
        billlabel.pack(pady=5)

        textarea = Text(root2, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
        textarea.pack(pady=5)
        textarea.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n\n')

        if costoffirst_aidvar.get() != '0 Rs':
            textarea.insert(END, f'Cost of First_aid\t\t\t{priceoffirst_aid}Rs\n')

        if costofsyrupsvar.get() != '0 Rs':
            textarea.insert(END, f'Cost of Syrups\t\t\t{priceofsyrups}Rs\n')

        if costofpillsvar.get() != '0 Rs':
            textarea.insert(END, f'Cost of Pills\t\t\t{priceofpills}Rs\n')

        textarea.insert(END, f'Sub Total\t\t\t{subtotalofitems}Rs\n')
        textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n')
        textarea.insert(END, f'Total Cost \t\t\t{subtotalofitems + 50}Rs\n')

        sendbutton = Button(root2, text='SEND', font=('arial', 19, 'bold'), bg='white', fg='red4', bd=7, relief=GROOVE,
                            command=send_msg)
        sendbutton.pack(pady=5)

        root2.mainloop()


def save():
    if textreciept.get(1.0, END) == '\n':
        pass
    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if url==None:
            pass
        else:

            bill_data = textreciept.get(1.0, END)
            url.write(bill_data)
            url.close()

            messagebox.showinfo('Information', 'Your Bill is Successfully Saved')



def receipt():
    global billnumber, date
    if costoffirst_aidvar.get() != '' or costofsyrupsvar.get() != '' or costofpillsvar.get() != '':
       textreciept.delete(1.0, END)
       x = random.randint(100, 10000)
       billnumber = 'BILL' + str(x)
       date = time.strftime('%d/%m/%y')
       textreciept.insert(END, 'Receipt Ref:\t\t' + billnumber+'\t\t' + date + '\n')
       textreciept.insert(END, '**************************************************************' + '\n')
       textreciept.insert(END, 'Items:\t\t Cost of Items(Rs) \n')
       textreciept.insert(END, '**************************************************************\n')
       if e_bandage.get()!='0':
          textreciept.insert(END, f'Bandage\t\t\t{int(e_bandage.get())*10}\n\n')

       if e_dettol.get()!='0':
          textreciept.insert(END, f'Dettol\t\t\t{int(e_dettol.get())*1}\n\n')


       if e_sticky_tape.get()!='0':
          textreciept.insert(END, f'Sticky_Tape\t\t\t{int(e_sticky_tape.get())*360}\n\n')


       if e_thermometer.get()!='0':
          textreciept.insert(END, f'Thermometer\t\t\t{int(e_thermometer.get())*180}\n\n')


       if e_tweezers.get()!='0':
          textreciept.insert(END, f'Tweezers\t\t\t{int(e_tweezers.get())*5}\n\n')


       if e_spray.get()!='0':
          textreciept.insert(END, f'Spray\t\t\t{int(e_spray.get())*10}\n\n')


       if e_diapers.get()!='0':
          textreciept.insert(END, f'Diapers\t\t\t{int(e_diapers.get())*10}\n\n')


       if e_condom.get()!='0':
          textreciept.insert(END, f'Condom\t\t\t{int(e_condom.get())*10}\n\n')


       if e_cotton.get()!='0':
          textreciept.insert(END, f'Cotton\t\t\t{int(e_cotton.get())*10}\n\n')


       if e_cofsils.get()!='0':
          textreciept.insert(END, f'Cofsils\t\t\t{int(e_cofsils.get())*760}\n\n')


       if e_benadryl.get()!='0':
          textreciept.insert(END, f'Benadryl\t\t\t{int(e_benadryl.get())*160}\n\n')


       if e_haldi_kuf.get()!='0':
          textreciept.insert(END, f'Haldi_Kuf\t\t\t{int(e_haldi_kuf.get())*90}\n\n')


       if e_d_15.get()!='0':
          textreciept.insert(END, f'd_15\t\t\t{int(e_d_15.get())*280}\n\n')


       if e_babuline.get()!='0':
          textreciept.insert(END, f'babuline\t\t\t{int(e_babuline.get())*75}\n\n')


       if e_ccf.get()!='0':
          textreciept.insert(END, f'CCF\t\t\t{int(e_ccf.get())*200}\n\n')


       if e_tusq.get()!='0':
          textreciept.insert(END, f'TusQ\t\t\t{int(e_tusq.get())*195}\n\n')


       if e_kofnil.get()!='0':
          textreciept.insert(END, f'Kofnil\t\t\t{int(e_kofnil.get())*490}\n\n')


       if e_codral.get()!='0':
          textreciept.insert(END, f'Codral\t\t\t{int(e_codral.get())*160}\n\n')


       if e_mucinex_d.get()!='0':
          textreciept.insert(END, f'Mucinex_D\t\t\t{int(e_mucinex_d.get())*550}\n\n')


       if e_total.get()!='0':
          textreciept.insert(END, f'total\t\t\t{int(e_total.get())*360}\n\n')


       if e_afrin.get()!='0':
          textreciept.insert(END, f'Afrin\t\t\t{int(e_afrin.get())*150}\n\n')


       if e_sudafed.get()!='0':
          textreciept.insert(END, f'Sudafed\t\t\t{int(e_sudafed.get())*1200}\n\n')


       if e_dolo_650.get()!='0':
          textreciept.insert(END, f'Dolo_650\t\t\t{int(e_dolo_650.get())*300}\n\n')


       if e_paracetamol.get()!='0':
          textreciept.insert(END, f'Paracetamol\t\t\t{int(e_paracetamol.get())*100}\n\n')


       if e_codeine.get()!='0':
          textreciept.insert(END, f'Codeine\t\t\t{int(e_codeine.get())*136}\n\n')


       if e_robafen.get()!='0':
         textreciept.insert(END, f'Bandage\t\t\t{int(e_robafen.get())*440}\n\n')


       if e_hytuss.get()!='0':
         textreciept.insert(END, f'Hytuss\t\t\t{int(e_hytuss.get())*5}\n\n')

       textreciept.insert(END, '**************************************************************\n')

       if costoffirst_aidvar.get()!='0 Rs':
          textreciept.insert(END, f'Cost of First_aid\t\t\t{priceoffirst_aid}Rs\n\n')

       if costofsyrupsvar.get() != '0 Rs':
          textreciept.insert(END, f'Cost of Syrups\t\t\t{priceofsyrups}Rs\n\n')

       if costofpillsvar.get() != '0 Rs':
          textreciept.insert(END, f'Cost of Pills\t\t\t{priceofpills}Rs\n\n')


       textreciept.insert(END, f'Sub Total\t\t\t{subtotalofitems}Rs\n\n')
       textreciept.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
       textreciept.insert(END, f'Total Cost \t\t\t{subtotalofitems+50}Rs\n\n')
       textreciept.insert(END, '**************************************************************\n')




def totalcost():
    global priceoffirst_aid, priceofsyrups, priceofpills, subtotalofitems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
       var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
       var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
       var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
       var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
       var26.get() != 0 or var27.get() != 0:

       item1 = int(e_bandage.get())
       item2 = int(e_dettol.get())
       item3 = int(e_sticky_tape.get())
       item4 = int(e_thermometer.get())
       item5 = int(e_tweezers.get())
       item6 = int(e_spray.get())
       item7 = int(e_diapers.get())
       item8 = int(e_condom.get())
       item9 = int(e_cotton.get())
       item10 = int(e_cofsils.get())
       item11 = int(e_benadryl.get())
       item12 = int(e_haldi_kuf.get())
       item13 = int(e_d_15.get())
       item14 = int(e_babuline.get())
       item15 = int(e_ccf.get())
       item16 = int(e_tusq.get())
       item17 = int(e_kofnil.get())
       item18 = int(e_codral.get())
       item19 = int(e_mucinex_d.get())
       item20 = int(e_total.get())
       item21 = int(e_afrin.get())
       item22 = int(e_sudafed.get())
       item23 = int(e_dolo_650.get())
       item24 = int(e_paracetamol.get())
       item25 = int(e_codeine.get())
       item26 = int(e_robafen.get())
       item27 = int(e_hytuss.get())


       priceoffirst_aid = (item1*10)+(item2*1)+(item3*360)+(item4*180)+(item5*5)+(item6*10)+(item7*10)+(item8*10) + \
                       (item9*10)

       priceofsyrups = (item10*760)+(item11*160)+(item12*90)+(item13*280)+(item14*75)+(item15*200)+(item16*195) + \
                  (item17*490)+(item18*160)

       priceofpills = (item19*550)+(item20*360)+(item21*150)+(item22*1200)+(item23*300)+(item24*100)+(item25*136) + \
                       (item26*440)+(item27*5)

       costoffirst_aidvar.set(str(priceoffirst_aid) + 'Rs')
       costofsyrupsvar.set(str(priceofsyrups) + 'RS')
       costofpillsvar.set(str(priceofpills) + 'Rs')


       subtotalofitems = priceoffirst_aid + priceofsyrups + priceofpills
       subtotalvar.set(str(subtotalofitems) + 'Rs')

       servicetaxvar.set('50 Rs')

       totalcost = subtotalofitems + 50
       totalcostvar.set(str(totalcost) + 'Rs')

    else:
        messagebox.showerror('Error', 'No Item is selected')





def Bandage():
    if var1.get() == 1:
        textbandage.config(state=NORMAL)
        textbandage.delete(0, END)
        textbandage.focus()
    else:
        textbandage.config(state=DISABLED)
        e_bandage.set('0')

def Dettol():
    if var2.get() == 1:
        textdettol.config(state=NORMAL)
        textdettol.delete(0, END)
        textdettol.focus()
    else:
        textdettol.config(state=DISABLED)
        e_dettol.set('0')


def Sticky_Tape():
    if var3.get() == 1:
        textsticky_tape.config(state=NORMAL)
        textsticky_tape.delete(0, END)
        textsticky_tape.focus()
    else:
        textsticky_tape.config(state=DISABLED)
        e_sticky_tape.set('0')


def Thermometer():
    if var4.get() == 1:
        textthermometer.config(state=NORMAL)
        textthermometer.delete(0, END)
        textthermometer.focus()
    else:
        textthermometer.config(state=DISABLED)
        e_thermometer.set('0')


def Tweezers():
    if var5.get() == 1:
        texttweezers.config(state=NORMAL)
        texttweezers.delete(0, END)
        texttweezers.focus()
    else:
        texttweezers.config(state=DISABLED)
        e_tweezers.set('0')


def Spray():
    if var6.get() == 1:
        textspray.config(state=NORMAL)
        textspray.delete(0, END)
        textspray.focus()
    else:
        textspray.config(state=DISABLED)
        e_spray.set('0')


def Diapers():
    if var7.get() == 1:
        textdiapers.config(state=NORMAL)
        textdiapers.delete(0, END)
        textdiapers.focus()
    else:
        textdiapers.config(state=DISABLED)
        e_diapers.set('0')


def Condom():
    if var8.get() == 1:
        textcondom.config(state=NORMAL)
        textcondom.delete(0, END)
        textcondom.focus()
    else:
        textcondom.config(state=DISABLED)
        e_condom.set('0')


def Cotton():
    if var9.get() == 1:
        textcotton.config(state=NORMAL)
        textcotton.delete(0, END)
        textcotton.focus()
    else:
        textcotton.config(state=DISABLED)
        e_cotton.set('0')


def Cofsils():
    if var10.get() == 1:
        textcofsils.config(state=NORMAL)
        textcofsils.delete(0, END)
        textcofsils.focus()
    else:
        textcofsils.config(state=DISABLED)
        e_cofsils.set('0')



def Benadryl():
    if var11.get() == 1:
        textbenadryl.config(state=NORMAL)
        textbenadryl.delete(0, END)
        textbenadryl.focus()
    else:
        textbenadryl.config(state=DISABLED)
        e_benadryl.set('0')


def Haldi_Kuf():
    if var12.get() == 1:
        texthaldi_kuf.config(state=NORMAL)
        texthaldi_kuf.delete(0, END)
        texthaldi_kuf.focus()
    else:
        texthaldi_kuf.config(state=DISABLED)
        e_haldi_kuf.set('0')



def d_15():
    if var13.get() == 1:
        textd_15.config(state=NORMAL)
        textd_15.delete(0, END)
        textd_15.focus()
    else:
        textd_15.config(state=DISABLED)
        e_d_15.set('0')


def babuline():
    if var14.get() == 1:
        textbabuline.config(state=NORMAL)
        textbabuline.delete(0, END)
        textbabuline.focus()
    else:
        textbabuline.config(state=DISABLED)
        e_babuline.set('0')



def CCF():
    if var15.get() == 1:
        textccf.config(state=NORMAL)
        textccf.delete(0, END)
        textccf.focus()
    else:
        textccf.config(state=DISABLED)
        e_ccf.set('0')



def TusQ():
    if var16.get() == 1:
        texttusq.config(state=NORMAL)
        texttusq.delete(0, END)
        texttusq.focus()
    else:
        texttusq.config(state=DISABLED)
        e_tusq.set('0')



def Kofnil():
    if var17.get() == 1:
        textkofnil.config(state=NORMAL)
        textkofnil.delete(0, END)
        textkofnil.focus()
    else:
        textkofnil.config(state=DISABLED)
        e_kofnil.set('0')



def Codral():
    if var18.get() == 1:
        textcodral.config(state=NORMAL)
        textcodral.delete(0, END)
        textcodral.focus()
    else:
        textcodral.config(state=DISABLED)
        e_codral.set('0')



def Mucinex_D():
    if var19.get() == 1:
        textmucinex_d.config(state=NORMAL)
        textmucinex_d.delete(0, END)
        textmucinex_d.focus()
    else:
        textmucinex_d.config(state=DISABLED)
        e_mucinex_d.set('0')


def total():
    if var20.get() == 1:
        texttotal.config(state=NORMAL)
        texttotal.delete(0, END)
        texttotal.focus()
    else:
        texttotal.config(state=DISABLED)
        e_total.set('0')



def Afrin():
    if var21.get() == 1:
        textafrin.config(state=NORMAL)
        textafrin.delete(0, END)
        textafrin.focus()
    else:
        textafrin.config(state=DISABLED)
        e_afrin.set('0')



def Sudafed():
    if var22.get() == 1:
        textsudafed.config(state=NORMAL)
        textsudafed.delete(0, END)
        textsudafed.focus()
    else:
        textsudafed.config(state=DISABLED)
        e_sudafed.set('0')



def Dolo_650():
    if var23.get() == 1:
        textdolo_650.config(state=NORMAL)
        textdolo_650.delete(0, END)
        textdolo_650.focus()
    else:
        textdolo_650.config(state=DISABLED)
        e_dolo_650.set('0')



def Paracetamol():
    if var24.get() == 1:
        textparacetamol.config(state=NORMAL)
        textparacetamol.delete(0, END)
        textparacetamol.focus()
    else:
        textparacetamol.config(state=DISABLED)
        e_paracetamol.set('0')


def Codeine():
    if var25.get() == 1:
        textcodeine.config(state=NORMAL)
        textcodeine.delete(0, END)
        textcodeine.focus()
    else:
        textcodeine.config(state=DISABLED)
        e_codeine.set('0')



def Robafen():
    if var26.get() == 1:
        textrobafen.config(state=NORMAL)
        textrobafen.delete(0, END)
        textrobafen.focus()
    else:
        textrobafen.config(state=DISABLED)
        e_robafen.set('0')


def Hytuss():
    if var27.get() == 1:
        texthytuss.config(state=NORMAL)
        texthytuss.delete(0, END)
        texthytuss.focus()
    else:
        texthytuss.config(state=DISABLED)
        e_hytuss.set('0')







root = Tk()

root.geometry('1270x690+0+0')
root.resizable(False, False)
root.title('Brabha Medicalshop')

root.config(bg='midnight blue')

topFrame = Frame(root, bd=10, relief=RIDGE, bg='midnight blue')
topFrame.pack(side=TOP)

labelTitle = Label(topFrame, text='Brabha MedicalShop', font=('arial', 30, 'bold'), fg='green',
                   bg='black', width=51, bd=9)
labelTitle.grid(row=0, column=0)


# frames

menuFrame = Frame(root, bd=10, relief=RIDGE, bg='midnight blue')
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame, bd=4, relief=RIDGE, bg='midnight blue', pady=10)
costFrame.pack(side=BOTTOM)

first_aidFrame = LabelFrame(menuFrame, text='First_aid', font=('arial', 15, 'bold'), bd=10, relief=RIDGE,
                            fg='green')
first_aidFrame.pack(side=LEFT)

syrupsFrame = LabelFrame(menuFrame, text='Syrups', font=('arial', 15, 'bold'), bd=10, relief=RIDGE, fg='green')
syrupsFrame.pack(side=LEFT)

pillsFrame = LabelFrame(menuFrame, text='Pills', font=('arial', 15, 'bold'), bd=10, relief=RIDGE, fg='green')
pillsFrame.pack(side=LEFT)

rightFrame = Frame(root, bd=15, relief=RIDGE, bg='midnight blue')
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame, bd=1, relief=RIDGE, bg='midnight blue')
calculatorFrame.pack()

recieptFrame = Frame(rightFrame, bd=4, relief=RIDGE, bg='midnight blue')
recieptFrame.pack()

buttonFrame = Frame(rightFrame, bd=3, relief=RIDGE, bg='midnight blue')
buttonFrame.pack()

# Variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_bandage = StringVar()
e_dettol = StringVar()
e_sticky_tape = StringVar()
e_thermometer = StringVar()
e_tweezers = StringVar()
e_spray = StringVar()
e_diapers = StringVar()
e_condom = StringVar()
e_cotton = StringVar()
e_cofsils = StringVar()
e_benadryl = StringVar()
e_haldi_kuf = StringVar()
e_d_15 = StringVar()
e_babuline = StringVar()
e_ccf = StringVar()
e_tusq = StringVar()
e_kofnil = StringVar()
e_codral = StringVar()
e_mucinex_d = StringVar()
e_total = StringVar()
e_afrin = StringVar()
e_sudafed = StringVar()
e_dolo_650 = StringVar()
e_paracetamol = StringVar()
e_codeine = StringVar()
e_robafen = StringVar()
e_hytuss = StringVar()

costoffirst_aidvar = StringVar()
costofsyrupsvar = StringVar()
costofpillsvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()


e_bandage.set('0')
e_dettol.set('0')
e_sticky_tape.set('0')
e_thermometer.set('0')
e_tweezers.set('0')
e_spray.set('0')
e_diapers.set('0')
e_condom.set('0')
e_cotton.set('0')
e_cofsils.set('0')
e_benadryl.set('0')
e_haldi_kuf.set('0')
e_d_15.set('0')
e_babuline.set('0')
e_ccf.set('0')
e_tusq.set('0')
e_kofnil.set('0')
e_codral.set('0')
e_mucinex_d.set('0')
e_total.set('0')
e_afrin.set('0')
e_sudafed.set('0')
e_dolo_650.set('0')
e_paracetamol.set('0')
e_codeine.set('0')
e_robafen.set('0')
e_hytuss.set('0')






# First_aid

Bandage = Checkbutton(first_aidFrame, text='Bandage', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var1,
                      command=Bandage)
Bandage.grid(row=0, column=0, sticky=W)

Dettol = Checkbutton(first_aidFrame, text='Dettol', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                            variable=var2, command=Dettol)
Dettol.grid(row=1, column=0, sticky=W)


Sticky_Tape = Checkbutton(first_aidFrame, text='Sticky_Tape', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var3,
                      command=Sticky_Tape)
Sticky_Tape.grid(row=2, column=0, sticky=W)

Thermometer = Checkbutton(first_aidFrame, text='Thermometer', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var4,
                   command=Thermometer)
Thermometer.grid(row=3, column=0, sticky=W)

Tweezers = Checkbutton(first_aidFrame, text='Tweezers', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var5,
                   command=Tweezers)
Tweezers.grid(row=4, column=0, sticky=W)

Spray = Checkbutton(first_aidFrame, text='Spray', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var6,
                      command=Spray)
Spray.grid(row=5, column=0, sticky=W)

Diapers = Checkbutton(first_aidFrame, text='Diapers', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                       variable=var7, command=Diapers)
Diapers.grid(row=6, column=0, sticky=W)

Condom = Checkbutton(first_aidFrame, text='Condom', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                       variable=var8, command=Condom)
Condom.grid(row=7, column=0, sticky=W)

Cotton = Checkbutton(first_aidFrame, text='Cotton', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                       variable=var9, command=Cotton)
Cotton.grid(row=8, column=0, sticky=W)


# Entry Fields for First_aid Items

textbandage = Entry(first_aidFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_bandage)
textbandage.grid(row=0, column=1)

textdettol = Entry(first_aidFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED,
                          textvariable=e_dettol)
textdettol.grid(row=1, column=1)

textsticky_tape = Entry(first_aidFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_sticky_tape)
textsticky_tape.grid(row=2, column=1)

textthermometer = Entry(first_aidFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_thermometer)
textthermometer.grid(row=3, column=1)

texttweezers = Entry(first_aidFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_tweezers)
texttweezers.grid(row=4, column=1)

textspray = Entry(first_aidFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_spray)
textspray.grid(row=5, column=1)

textdiapers = Entry(first_aidFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_diapers)
textdiapers.grid(row=6, column=1)

textcondom = Entry(first_aidFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_condom)
textcondom.grid(row=7, column=1)

textcotton = Entry(first_aidFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_cotton)
textcotton.grid(row=8, column=1)


# Syrups

Cofsils = Checkbutton(syrupsFrame, text='Cofsils', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var10,
                      command=Cofsils)
Cofsils.grid(row=0, column=0, sticky=W)

Benadryl = Checkbutton(syrupsFrame, text='Benadryl', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                         variable=var11, command=Benadryl)
Benadryl.grid(row=1, column=0, sticky=W)

Haldi_Kuf = Checkbutton(syrupsFrame, text='Haldi_Kuf', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var12,
                     command=Haldi_Kuf)
Haldi_Kuf.grid(row=2, column=0, sticky=W)

d_15 = Checkbutton(syrupsFrame, text='D_15', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                           variable=var13, command=d_15)
d_15.grid(row=3, column=0, sticky=W)

babuline = Checkbutton(syrupsFrame, text='Babuline', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var14,
                     command=babuline)
babuline.grid(row=4, column=0, sticky=W)

CCF = Checkbutton(syrupsFrame, text='CCF', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var15,
                       command=CCF)
CCF.grid(row=5, column=0, sticky=W)

TusQ = Checkbutton(syrupsFrame, text='TusQ', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                              variable=var16, command=TusQ)
TusQ.grid(row=6, column=0, sticky=W)

Kofnil = Checkbutton(syrupsFrame, text='Kofnil', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                           variable=var17, command=Kofnil)
Kofnil.grid(row=7, column=0, sticky=W)


Codral = Checkbutton(syrupsFrame, text='Codral', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var18,
                        command=Codral)
Codral.grid(row=8, column=0, sticky=W)


# Entry Fields for Syrups Items

textcofsils = Entry(syrupsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_cofsils)
textcofsils.grid(row=0, column=1)

textbenadryl = Entry(syrupsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_benadryl)
textbenadryl.grid(row=1, column=1)

texthaldi_kuf = Entry(syrupsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_haldi_kuf)
texthaldi_kuf.grid(row=2, column=1)

textd_15 = Entry(syrupsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_d_15)
textd_15.grid(row=3, column=1)

textbabuline = Entry(syrupsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_babuline)
textbabuline.grid(row=4, column=1)

textccf = Entry(syrupsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_ccf)
textccf.grid(row=5, column=1)

texttusq = Entry(syrupsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_tusq)
texttusq.grid(row=6, column=1)

textkofnil = Entry(syrupsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED,
                    textvariable=e_kofnil)
textkofnil.grid(row=7, column=1)

textcodral = Entry(syrupsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_codral)
textcodral.grid(row=8, column=1)


# Pills

Mucinex_D = Checkbutton(pillsFrame, text='Mucinex_D', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                       variable=var19, command=Mucinex_D)
Mucinex_D.grid(row=0, column=0, sticky=W)

total = Checkbutton(pillsFrame, text='Total', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var20,
                    command=total)
total.grid(row=1, column=0, sticky=W)

Afrin = Checkbutton(pillsFrame, text='Afrin', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                        variable=var21, command=Afrin)
Afrin.grid(row=2, column=0, sticky=W)

Sudafed = Checkbutton(pillsFrame, text='Sudafed', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var22,
                    command=Sudafed)
Sudafed.grid(row=3, column=0, sticky=W)

Dolo_650 = Checkbutton(pillsFrame, text='Dolo_650', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var23,
                    command=Dolo_650)
Dolo_650.grid(row=4, column=0, sticky=W)

Paracetamol = Checkbutton(pillsFrame, text='Paracetamol', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                       variable=var24, command=Paracetamol)
Paracetamol.grid(row=5, column=0, sticky=W)

Codeine = Checkbutton(pillsFrame, text='Codeine', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var25,
                    command=Codeine)
Codeine.grid(row=6, column=0, sticky=W)

Robafen = Checkbutton(pillsFrame, text='Robafen', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var26,
                    command=Robafen)
Robafen.grid(row=7, column=0, sticky=W)

Hytuss = Checkbutton(pillsFrame, text='Hytuss', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                        variable=var27, command=Hytuss)
Hytuss.grid(row=8, column=0, sticky=W)


# Entry Field for Pills Items

textmucinex_d = Entry(pillsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_mucinex_d)
textmucinex_d.grid(row=0, column=1)

texttotal = Entry(pillsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_total)
texttotal.grid(row=1, column=1)

textafrin = Entry(pillsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED,
                      textvariable=e_afrin)
textafrin.grid(row=2, column=1)

textsudafed = Entry(pillsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_sudafed)
textsudafed.grid(row=3, column=1)

textdolo_650 = Entry(pillsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_dolo_650)
textdolo_650.grid(row=4, column=1)

textparacetamol = Entry(pillsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_paracetamol)
textparacetamol.grid(row=5, column=1)

textcodeine = Entry(pillsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_codeine)
textcodeine.grid(row=6, column=1)

textrobafen = Entry(pillsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_robafen)
textrobafen.grid(row=7, column=1)

texthytuss = Entry(pillsFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED,
                      textvariable=e_hytuss)
texthytuss.grid(row=8, column=1)



# CostLabels & entry firlds

labelcostoffirst_aid = Label(costFrame, text='Cost of First_aid', font=('arial', 16, 'bold'), bg='midnight blue',
                             fg='white')
labelcostoffirst_aid.grid(row=0, column=0)


textcostoffirst_aid = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                            textvariable=costoffirst_aidvar)
textcostoffirst_aid.grid(row=0, column=1, padx=41)


labelcostofsyrups = Label(costFrame, text='Cost of Syrups', font=('arial', 16, 'bold'), bg='midnight blue', fg='white')
labelcostofsyrups.grid(row=1, column=0)

textcostofsyrups = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                       textvariable=costofsyrupsvar)
textcostofsyrups.grid(row=1, column=1, padx=41)


labelcostofpills = Label(costFrame, text='Cost of Pills', font=('arial', 16, 'bold'), bg='midnight blue',
                             fg='white')
labelcostofpills.grid(row=2, column=0)

textcostofpills = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                            textvariable=costofpillsvar)
textcostofpills.grid(row=2, column=1, padx=41)


labelsubtotal = Label(costFrame, text='Sub Total', font=('arial', 16, 'bold'), bg='midnight blue', fg='white')
labelsubtotal.grid(row=0, column=2)

textsubtotal = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly', textvariable=subtotalvar)
textsubtotal.grid(row=0, column=3, padx=41)


labelservicetax = Label(costFrame, text='Service Tax', font=('arial', 16, 'bold'), bg='midnight blue', fg='white')
labelservicetax.grid(row=1, column=2)

textservicetax = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                       textvariable=servicetaxvar)
textservicetax.grid(row=1, column=3, padx=41)


labeltotal = Label(costFrame, text='Total Cost', font=('arial', 16, 'bold'), bg='midnight blue', fg='white')
labeltotal.grid(row=2, column=2)

texttotalcost = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                      textvariable=totalcostvar)
texttotalcost.grid(row=2, column=3, padx=41)



# Buttons

buttontotal = Button(buttonFrame, text='Total', font=('arial', 14, 'bold'), fg='white', bg='midnight blue', bd=1,
                     padx=5, command=totalcost)
buttontotal.grid(row=0, column=0)

buttonreciept = Button(buttonFrame, text='Reciept', font=('arial', 14, 'bold'), fg='white', bg='midnight blue', bd=1,
                       padx=5, command=receipt)
buttonreciept.grid(row=0, column=1)

buttonsave = Button(buttonFrame, text='Save', font=('arial', 14, 'bold'), fg='white', bg='midnight blue', bd=1, padx=5,
                    command=save)
buttonsave.grid(row=0, column=2)

buttonsend = Button(buttonFrame, text='Send', font=('arial', 14, 'bold'), fg='white', bg='midnight blue', bd=1, padx=5,
                    command=send)
buttonsend.grid(row=0, column=3)

buttonreset = Button(buttonFrame, text='Reset', font=('arial', 14, 'bold'), fg='white', bg='midnight blue', bd=1,
                     padx=5, command=reset)
buttonreset.grid(row=0, column=4)


# text area for receipt

textreciept = Text(recieptFrame, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
textreciept.grid(row=0, column=0)


# calculator

operator = ''
def buttonClick(numbers):
    global operator
    operator = operator+numbers
    calculatorfield.delete(0, END)
    calculatorfield.insert(END, operator)


def clear():
    global operator
    operator = ''
    calculatorfield.delete(0, END)


def answer():
    global operator
    result = str(eval(operator))
    calculatorfield.delete(0, END)
    calculatorfield.insert(0, result)
    operator = ''


calculatorfield = Entry(calculatorFrame, font=('arial', 16, 'bold'), width=32, bd=1)
calculatorfield.grid(row=0, column=0, columnspan=4)


button7 = Button(calculatorFrame, text='7', font=('arial', 16, 'bold'), fg='red4', bg='black', bd=2, width=6,
                 command=lambda: buttonClick('7'))
button7.grid(row=1, column=0)

button8 = Button(calculatorFrame, text='8', font=('arial', 16, 'bold'), fg='red4', bg='black', bd=2, width=6,
                 command=lambda: buttonClick('8'))
button8.grid(row=1, column=1)

button9 = Button(calculatorFrame, text='9', font=('arial', 16, 'bold'), fg='red4', bg='black', bd=2, width=6,
                 command=lambda: buttonClick('9'))
button9.grid(row=1, column=2)

buttonplus = Button(calculatorFrame, text='+', font=('arial', 16, 'bold'), fg='red4', bg='black', bd=2, width=6,
                    command=lambda: buttonClick('+'))
buttonplus.grid(row=1, column=3)

button4 = Button(calculatorFrame, text='4', font=('arial', 16, 'bold'), fg='red4', bg='black', bd=2, width=6,
                 command=lambda: buttonClick('4'))
button4.grid(row=2, column=0)

button5 = Button(calculatorFrame, text='5', font=('arial', 16, 'bold'), fg='blue', bg='white', bd=2, width=6,
                 command=lambda: buttonClick('5'))
button5.grid(row=2, column=1)

button6 = Button(calculatorFrame, text='6', font=('arial', 16, 'bold'), fg='blue', bg='white', bd=2, width=6,
                 command=lambda: buttonClick('6'))
button6.grid(row=2, column=2)

buttonminus = Button(calculatorFrame, text='-', font=('arial', 16, 'bold'), fg='red4', bg='black', bd=2, width=6,
                     command=lambda: buttonClick('-'))
buttonminus.grid(row=2, column=3)

button1 = Button(calculatorFrame, text='1', font=('arial', 16, 'bold'), fg='red4', bg='black', bd=2, width=6,
                 command=lambda: buttonClick('1'))
button1.grid(row=3, column=0)

button2 = Button(calculatorFrame, text='2', font=('arial', 16, 'bold'), fg='blue', bg='white', bd=2, width=6,
                 command=lambda: buttonClick('2'))
button2.grid(row=3, column=1)

button3 = Button(calculatorFrame, text='3', font=('arial', 16, 'bold'), fg='blue', bg='white', bd=2, width=6,
                 command=lambda: buttonClick('3'))
button3.grid(row=3, column=2)

buttonmult = Button(calculatorFrame, text='*', font=('arial', 16, 'bold'), fg='red4', bg='black', bd=2, width=6,
                    command=lambda: buttonClick('*'))
buttonmult.grid(row=3, column=3)

buttonans = Button(calculatorFrame, text='Ans', font=('arial', 16, 'bold'), fg='red4', bg='black', bd=2, width=6,
                   command=answer)
buttonans.grid(row=4, column=0)

buttonclear = Button(calculatorFrame, text='Clear', font=('arial', 16, 'bold'), fg='red4', bg='black', bd=2, width=6,
                     command=clear)
buttonclear.grid(row=4, column=1)

button0 = Button(calculatorFrame, text='0', font=('arial', 16, 'bold'), fg='red4', bg='black', bd=2, width=6,
                 command=lambda: buttonClick('0'))
button0.grid(row=4, column=2)

buttondiv = Button(calculatorFrame, text='/', font=('arial', 16, 'bold'), fg='red4', bg='black', bd=2, width=6,
                   command=lambda: buttonClick('/'))
buttondiv.grid(row=4, column=3)













root.mainloop()