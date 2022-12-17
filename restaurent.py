import random
import time
from tkinter import *
from   tkinter import filedialog, messagebox
import requests


# Functions


def reset():
    textreciept.delete(1.0, END)
    e_mixture.set('0')
    e_garlic_pickle.set('0')
    e_chicken.set('0')
    e_fish.set('0')
    e_lays.set('0')
    e_kadalai.set('0')
    e_karachuv.set('0')
    e_omelette.set('0')
    e_halfboil.set('0')
    e_oldmonk.set('0')
    e_kingfisher.set('0')
    e_tuborg.set('0')
    e_samual_adams.set('0')
    e_indian.set('0')
    e_bluemoon.set('0')
    e_budweisermagnum.set('0')
    e_budlightlime.set('0')
    e_carlsberg.set('0')
    e_marlboro.set('0')
    e_total.set('0')
    e_goldflake.set('0')
    e_royal.set('0')
    e_kings.set('0')
    e_scissors.set('0')
    e_wills.set('0')
    e_camel.set('0')
    e_kajabeedi.set('0')



    textmixture.config(state=DISABLED)
    textgarlic_pickle.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textlays.config(state=DISABLED)
    textkadalai.config(state=DISABLED)
    textkarachuv.config(state=DISABLED)
    textomelette.config(state=DISABLED)
    texthalfboil.config(state=DISABLED)
    textoldmonk.config(state=DISABLED)
    textkingfisher.config(state=DISABLED)
    texttuborg.config(state=DISABLED)
    textsamual_adams.config(state=DISABLED)
    textindian.config(state=DISABLED)
    textbluemoon.config(state=DISABLED)
    textbudweisermagnum.config(state=DISABLED)
    textbudlightlime.config(state=DISABLED)
    textcarlsberg.config(state=DISABLED)
    textmarlboro.config(state=DISABLED)
    texttotal.config(state=DISABLED)
    textgoldflake.config(state=DISABLED)
    textroyal.config(state=DISABLED)
    textkings.config(state=DISABLED)
    textscissors.config(state=DISABLED)
    textwills.config(state=DISABLED)
    textcamel.config(state=DISABLED)
    textkajabeedi.config(state=DISABLED)

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


    costofside_dishvar.set('')
    costofbeervar.set('')
    costofcigarettevar.set('')
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

        if costofside_dishvar.get() != '0 Rs':
            textarea.insert(END, f'Cost of Side_Dish\t\t\t{priceofside_dish}Rs\n')

        if costofbeervar.get() != '0 Rs':
            textarea.insert(END, f'Cost of BEER\t\t\t{priceofbeer}Rs\n')

        if costofcigarettevar.get() != '0 Rs':
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
    if costofside_dishvar.get() != '' or costofbeervar.get() != '' or costofcigarettevar.get() != '':
       textreciept.delete(1.0, END)
       x = random.randint(100, 10000)
       billnumber = 'BILL' + str(x)
       date = time.strftime('%d/%m/%y')
       textreciept.insert(END, 'Receipt Ref:\t\t' + billnumber+'\t\t' + date + '\n')
       textreciept.insert(END, '**************************************************************' + '\n')
       textreciept.insert(END, 'Items:\t\t Cost of Items(Rs) \n')
       textreciept.insert(END, '**************************************************************\n')
       if e_mixture.get()!='0':
          textreciept.insert(END, f'mixture\t\t\t{int(e_mixture.get())*10}\n\n')

       if e_garlic_pickle.get()!='0':
          textreciept.insert(END, f'garlic_pickle\t\t\t{int(e_garlic_pickle.get())*1}\n\n')


       if e_chicken.get()!='0':
          textreciept.insert(END, f'chicken\t\t\t{int(e_chicken.get())*360}\n\n')


       if e_fish.get()!='0':
          textreciept.insert(END, f'fish\t\t\t{int(e_fish.get())*180}\n\n')


       if e_lays.get()!='0':
          textreciept.insert(END, f'lays\t\t\t{int(e_lays.get())*5}\n\n')


       if e_kadalai.get()!='0':
          textreciept.insert(END, f'kadalai\t\t\t{int(e_kadalai.get())*10}\n\n')


       if e_karachuv.get()!='0':
          textreciept.insert(END, f'karachuv\t\t\t{int(e_karachuv.get())*10}\n\n')


       if e_omelette.get()!='0':
          textreciept.insert(END, f'omelette\t\t\t{int(e_omelette.get())*10}\n\n')


       if e_halfboil.get()!='0':
          textreciept.insert(END, f'halfboil\t\t\t{int(e_halfboil.get())*10}\n\n')


       if e_oldmonk.get()!='0':
          textreciept.insert(END, f'oldmonk\t\t\t{int(e_oldmonk.get())*760}\n\n')


       if e_kingfisher.get()!='0':
          textreciept.insert(END, f'kingfisher\t\t\t{int(e_kingfisher.get())*160}\n\n')


       if e_tuborg.get()!='0':
          textreciept.insert(END, f'tuborg\t\t\t{int(e_tuborg.get())*90}\n\n')


       if e_samual_adams.get()!='0':
          textreciept.insert(END, f'samual_adams\t\t\t{int(e_samual_adams.get())*280}\n\n')


       if e_indian.get()!='0':
          textreciept.insert(END, f'indian\t\t\t{int(e_indian.get())*75}\n\n')


       if e_bluemoon.get()!='0':
          textreciept.insert(END, f'bluemoon\t\t\t{int(e_bluemoon.get())*200}\n\n')


       if e_budweisermagnum.get()!='0':
          textreciept.insert(END, f'budweisermagnum\t\t\t{int(e_budweisermagnum.get())*195}\n\n')


       if e_budlightlime.get()!='0':
          textreciept.insert(END, f'budlightlime\t\t\t{int(e_budlightlime.get())*490}\n\n')


       if e_carlsberg.get()!='0':
          textreciept.insert(END, f'carlsberg\t\t\t{int(e_carlsberg.get())*160}\n\n')


       if e_marlboro.get()!='0':
          textreciept.insert(END, f'marlboro\t\t\t{int(e_marlboro.get())*550}\n\n')


       if e_total.get()!='0':
          textreciept.insert(END, f'total\t\t\t{int(e_total.get())*360}\n\n')


       if e_goldflake.get()!='0':
          textreciept.insert(END, f'goldflake\t\t\t{int(e_goldflake.get())*150}\n\n')


       if e_royal.get()!='0':
          textreciept.insert(END, f'royal\t\t\t{int(e_royal.get())*1200}\n\n')


       if e_kings.get()!='0':
          textreciept.insert(END, f'kings\t\t\t{int(e_kings.get())*300}\n\n')


       if e_scissors.get()!='0':
          textreciept.insert(END, f'scissors\t\t\t{int(e_scissors.get())*100}\n\n')


       if e_wills.get()!='0':
          textreciept.insert(END, f'wills\t\t\t{int(e_wills.get())*136}\n\n')


       if e_camel.get()!='0':
         textreciept.insert(END, f'mixture\t\t\t{int(e_camel.get())*440}\n\n')


       if e_kajabeedi.get()!='0':
         textreciept.insert(END, f'kajabeedi\t\t\t{int(e_kajabeedi.get())*5}\n\n')

       textreciept.insert(END, '**************************************************************\n')

       if costofside_dishvar.get()!='0 Rs':
          textreciept.insert(END, f'Cost of Side_Dish\t\t\t{priceofside_dish}Rs\n\n')

       if costofbeervar.get() != '0 Rs':
          textreciept.insert(END, f'Cost of BEER\t\t\t{priceofbeer}Rs\n\n')

       if costofcigarettevar.get() != '0 Rs':
          textreciept.insert(END, f'Cost of Pills\t\t\t{priceofpills}Rs\n\n')


       textreciept.insert(END, f'Sub Total\t\t\t{subtotalofitems}Rs\n\n')
       textreciept.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
       textreciept.insert(END, f'Total Cost \t\t\t{subtotalofitems+50}Rs\n\n')
       textreciept.insert(END, '**************************************************************\n')




def totalcost():
    global priceofside_dish, priceofbeer, priceofpills, subtotalofitems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
       var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
       var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
       var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
       var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
       var26.get() != 0 or var27.get() != 0:

       item1 = int(e_mixture.get())
       item2 = int(e_garlic_pickle.get())
       item3 = int(e_chicken.get())
       item4 = int(e_fish.get())
       item5 = int(e_lays.get())
       item6 = int(e_kadalai.get())
       item7 = int(e_karachuv.get())
       item8 = int(e_omelette.get())
       item9 = int(e_halfboil.get())
       item10 = int(e_oldmonk.get())
       item11 = int(e_kingfisher.get())
       item12 = int(e_tuborg.get())
       item13 = int(e_samual_adams.get())
       item14 = int(e_indian.get())
       item15 = int(e_bluemoon.get())
       item16 = int(e_budweisermagnum.get())
       item17 = int(e_budlightlime.get())
       item18 = int(e_carlsberg.get())
       item19 = int(e_marlboro.get())
       item20 = int(e_total.get())
       item21 = int(e_goldflake.get())
       item22 = int(e_royal.get())
       item23 = int(e_kings.get())
       item24 = int(e_scissors.get())
       item25 = int(e_wills.get())
       item26 = int(e_camel.get())
       item27 = int(e_kajabeedi.get())


       priceofside_dish = (item1*10)+(item2*1)+(item3*360)+(item4*180)+(item5*5)+(item6*10)+(item7*10)+(item8*10) + \
                       (item9*10)

       priceofbeer = (item10*760)+(item11*160)+(item12*90)+(item13*280)+(item14*75)+(item15*200)+(item16*195) + \
                  (item17*490)+(item18*160)

       priceofpills = (item19*550)+(item20*360)+(item21*150)+(item22*1200)+(item23*300)+(item24*100)+(item25*136) + \
                       (item26*440)+(item27*5)

       costofside_dishvar.set(str(priceofside_dish) + 'Rs')
       costofbeervar.set(str(priceofbeer) + 'RS')
       costofcigarettevar.set(str(priceofpills) + 'Rs')


       subtotalofitems = priceofside_dish + priceofbeer + priceofpills
       subtotalvar.set(str(subtotalofitems) + 'Rs')

       servicetaxvar.set('50 Rs')

       totalcost = subtotalofitems + 50
       totalcostvar.set(str(totalcost) + 'Rs')

    else:
        messagebox.showerror('Error', 'No Item is selected')





def mixture():
    if var1.get() == 1:
        textmixture.config(state=NORMAL)
        textmixture.delete(0, END)
        textmixture.focus()
    else:
        textmixture.config(state=DISABLED)
        e_mixture.set('0')

def garlic_pickle():
    if var2.get() == 1:
        textgarlic_pickle.config(state=NORMAL)
        textgarlic_pickle.delete(0, END)
        textgarlic_pickle.focus()
    else:
        textgarlic_pickle.config(state=DISABLED)
        e_garlic_pickle.set('0')


def chicken():
    if var3.get() == 1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0, END)
        textchicken.focus()
    else:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')


def fish():
    if var4.get() == 1:
        textfish.config(state=NORMAL)
        textfish.delete(0, END)
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')


def lays():
    if var5.get() == 1:
        textlays.config(state=NORMAL)
        textlays.delete(0, END)
        textlays.focus()
    else:
        textlays.config(state=DISABLED)
        e_lays.set('0')


def kadalai():
    if var6.get() == 1:
        textkadalai.config(state=NORMAL)
        textkadalai.delete(0, END)
        textkadalai.focus()
    else:
        textkadalai.config(state=DISABLED)
        e_kadalai.set('0')


def karachuv():
    if var7.get() == 1:
        textkarachuv.config(state=NORMAL)
        textkarachuv.delete(0, END)
        textkarachuv.focus()
    else:
        textkarachuv.config(state=DISABLED)
        e_karachuv.set('0')


def omelette():
    if var8.get() == 1:
        textomelette.config(state=NORMAL)
        textomelette.delete(0, END)
        textomelette.focus()
    else:
        textomelette.config(state=DISABLED)
        e_omelette.set('0')


def halfboil():
    if var9.get() == 1:
        texthalfboil.config(state=NORMAL)
        texthalfboil.delete(0, END)
        texthalfboil.focus()
    else:
        texthalfboil.config(state=DISABLED)
        e_halfboil.set('0')


def oldmonk():
    if var10.get() == 1:
        textoldmonk.config(state=NORMAL)
        textoldmonk.delete(0, END)
        textoldmonk.focus()
    else:
        textoldmonk.config(state=DISABLED)
        e_oldmonk.set('0')



def kingfisher():
    if var11.get() == 1:
        textkingfisher.config(state=NORMAL)
        textkingfisher.delete(0, END)
        textkingfisher.focus()
    else:
        textkingfisher.config(state=DISABLED)
        e_kingfisher.set('0')


def tuborg():
    if var12.get() == 1:
        texttuborg.config(state=NORMAL)
        texttuborg.delete(0, END)
        texttuborg.focus()
    else:
        texttuborg.config(state=DISABLED)
        e_tuborg.set('0')



def samual_adams():
    if var13.get() == 1:
        textsamual_adams.config(state=NORMAL)
        textsamual_adams.delete(0, END)
        textsamual_adams.focus()
    else:
        textsamual_adams.config(state=DISABLED)
        e_samual_adams.set('0')


def indian():
    if var14.get() == 1:
        textindian.config(state=NORMAL)
        textindian.delete(0, END)
        textindian.focus()
    else:
        textindian.config(state=DISABLED)
        e_indian.set('0')



def bluemoon():
    if var15.get() == 1:
        textbluemoon.config(state=NORMAL)
        textbluemoon.delete(0, END)
        textbluemoon.focus()
    else:
        textbluemoon.config(state=DISABLED)
        e_bluemoon.set('0')



def budweisermagnum():
    if var16.get() == 1:
        textbudweisermagnum.config(state=NORMAL)
        textbudweisermagnum.delete(0, END)
        textbudweisermagnum.focus()
    else:
        textbudweisermagnum.config(state=DISABLED)
        e_budweisermagnum.set('0')



def budlightlime():
    if var17.get() == 1:
        textbudlightlime.config(state=NORMAL)
        textbudlightlime.delete(0, END)
        textbudlightlime.focus()
    else:
        textbudlightlime.config(state=DISABLED)
        e_budlightlime.set('0')



def carlsberg():
    if var18.get() == 1:
        textcarlsberg.config(state=NORMAL)
        textcarlsberg.delete(0, END)
        textcarlsberg.focus()
    else:
        textcarlsberg.config(state=DISABLED)
        e_carlsberg.set('0')



def marlboro():
    if var19.get() == 1:
        textmarlboro.config(state=NORMAL)
        textmarlboro.delete(0, END)
        textmarlboro.focus()
    else:
        textmarlboro.config(state=DISABLED)
        e_marlboro.set('0')


def total():
    if var20.get() == 1:
        texttotal.config(state=NORMAL)
        texttotal.delete(0, END)
        texttotal.focus()
    else:
        texttotal.config(state=DISABLED)
        e_total.set('0')



def goldflake():
    if var21.get() == 1:
        textgoldflake.config(state=NORMAL)
        textgoldflake.delete(0, END)
        textgoldflake.focus()
    else:
        textgoldflake.config(state=DISABLED)
        e_goldflake.set('0')



def royal():
    if var22.get() == 1:
        textroyal.config(state=NORMAL)
        textroyal.delete(0, END)
        textroyal.focus()
    else:
        textroyal.config(state=DISABLED)
        e_royal.set('0')



def kings():
    if var23.get() == 1:
        textkings.config(state=NORMAL)
        textkings.delete(0, END)
        textkings.focus()
    else:
        textkings.config(state=DISABLED)
        e_kings.set('0')



def scissors():
    if var24.get() == 1:
        textscissors.config(state=NORMAL)
        textscissors.delete(0, END)
        textscissors.focus()
    else:
        textscissors.config(state=DISABLED)
        e_scissors.set('0')


def wills():
    if var25.get() == 1:
        textwills.config(state=NORMAL)
        textwills.delete(0, END)
        textwills.focus()
    else:
        textwills.config(state=DISABLED)
        e_wills.set('0')



def camel():
    if var26.get() == 1:
        textcamel.config(state=NORMAL)
        textcamel.delete(0, END)
        textcamel.focus()
    else:
        textcamel.config(state=DISABLED)
        e_camel.set('0')


def kajabeedi():
    if var27.get() == 1:
        textkajabeedi.config(state=NORMAL)
        textkajabeedi.delete(0, END)
        textkajabeedi.focus()
    else:
        textkajabeedi.config(state=DISABLED)
        e_kajabeedi.set('0')







root = Tk()

root.geometry('1270x690+0+0')
root.resizable(False, False)
root.title('Brabha Wineshop')

root.config(bg='midnight blue')

topFrame = Frame(root, bd=10, relief=RIDGE, bg='midnight blue')
topFrame.pack(side=TOP)

labelTitle = Label(topFrame, text='Brabha WineShop', font=('arial', 30, 'bold'), fg='green',
                   bg='black', width=51, bd=9)
labelTitle.grid(row=0, column=0)


# frames

menuFrame = Frame(root, bd=10, relief=RIDGE, bg='midnight blue')
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame, bd=4, relief=RIDGE, bg='midnight blue', pady=10)
costFrame.pack(side=BOTTOM)

side_dishFrame = LabelFrame(menuFrame, text='Side_Dish', font=('arial', 15, 'bold'), bd=10, relief=RIDGE,
                            fg='green')
side_dishFrame.pack(side=LEFT)

beerFrame = LabelFrame(menuFrame, text='Beer', font=('arial', 15, 'bold'), bd=10, relief=RIDGE, fg='green')
beerFrame.pack(side=LEFT)

cigaretteFrame = LabelFrame(menuFrame, text='Cigarette', font=('arial', 15, 'bold'), bd=10, relief=RIDGE, fg='green')
cigaretteFrame.pack(side=LEFT)

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

e_mixture = StringVar()
e_garlic_pickle = StringVar()
e_chicken = StringVar()
e_fish = StringVar()
e_lays = StringVar()
e_kadalai = StringVar()
e_karachuv = StringVar()
e_omelette = StringVar()
e_halfboil = StringVar()
e_oldmonk = StringVar()
e_kingfisher = StringVar()
e_tuborg = StringVar()
e_samual_adams = StringVar()
e_indian = StringVar()
e_bluemoon = StringVar()
e_budweisermagnum = StringVar()
e_budlightlime = StringVar()
e_carlsberg = StringVar()
e_marlboro = StringVar()
e_total = StringVar()
e_goldflake = StringVar()
e_royal = StringVar()
e_kings = StringVar()
e_scissors = StringVar()
e_wills = StringVar()
e_camel = StringVar()
e_kajabeedi = StringVar()

costofside_dishvar = StringVar()
costofbeervar = StringVar()
costofcigarettevar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()


e_mixture.set('0')
e_garlic_pickle.set('0')
e_chicken.set('0')
e_fish.set('0')
e_lays.set('0')
e_kadalai.set('0')
e_karachuv.set('0')
e_omelette.set('0')
e_halfboil.set('0')
e_oldmonk.set('0')
e_kingfisher.set('0')
e_tuborg.set('0')
e_samual_adams.set('0')
e_indian.set('0')
e_bluemoon.set('0')
e_budweisermagnum.set('0')
e_budlightlime.set('0')
e_carlsberg.set('0')
e_marlboro.set('0')
e_total.set('0')
e_goldflake.set('0')
e_royal.set('0')
e_kings.set('0')
e_scissors.set('0')
e_wills.set('0')
e_camel.set('0')
e_kajabeedi.set('0')






# Side_Dish

mixture = Checkbutton(side_dishFrame, text='Mixture', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var1,
                      command=mixture)
mixture.grid(row=0, column=0, sticky=W)

garlic_pickle = Checkbutton(side_dishFrame, text='Garlic_Pickle', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                            variable=var2, command=garlic_pickle)
garlic_pickle.grid(row=1, column=0, sticky=W)


chicken = Checkbutton(side_dishFrame, text='Chicken', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var3,
                      command=chicken)
chicken.grid(row=2, column=0, sticky=W)

fish = Checkbutton(side_dishFrame, text='Fish', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var4,
                   command=fish)
fish.grid(row=3, column=0, sticky=W)

lays = Checkbutton(side_dishFrame, text='Lays', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var5,
                   command=lays)
lays.grid(row=4, column=0, sticky=W)

kadalai = Checkbutton(side_dishFrame, text='Kadalai', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var6,
                      command=kadalai)
kadalai.grid(row=5, column=0, sticky=W)

karachuv = Checkbutton(side_dishFrame, text='Karachuv', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                       variable=var7, command=karachuv)
karachuv.grid(row=6, column=0, sticky=W)

omelette = Checkbutton(side_dishFrame, text='Omelette', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                       variable=var8, command=omelette)
omelette.grid(row=7, column=0, sticky=W)

halfboil = Checkbutton(side_dishFrame, text='HalfBoil', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                       variable=var9, command=halfboil)
halfboil.grid(row=8, column=0, sticky=W)


# Entry Fields for Side_Dish Items

textmixture = Entry(side_dishFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_mixture)
textmixture.grid(row=0, column=1)

textgarlic_pickle = Entry(side_dishFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED,
                          textvariable=e_garlic_pickle)
textgarlic_pickle.grid(row=1, column=1)

textchicken = Entry(side_dishFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_chicken)
textchicken.grid(row=2, column=1)

textfish = Entry(side_dishFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_fish)
textfish.grid(row=3, column=1)

textlays = Entry(side_dishFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_lays)
textlays.grid(row=4, column=1)

textkadalai = Entry(side_dishFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_kadalai)
textkadalai.grid(row=5, column=1)

textkarachuv = Entry(side_dishFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_karachuv)
textkarachuv.grid(row=6, column=1)

textomelette = Entry(side_dishFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_omelette)
textomelette.grid(row=7, column=1)

texthalfboil = Entry(side_dishFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_halfboil)
texthalfboil.grid(row=8, column=1)


# Beer

oldmonk = Checkbutton(beerFrame, text='OldMonk', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var10,
                      command=oldmonk)
oldmonk.grid(row=0, column=0, sticky=W)

kingfisher = Checkbutton(beerFrame, text='KingFisher', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                         variable=var11, command=kingfisher)
kingfisher.grid(row=1, column=0, sticky=W)

tuborg = Checkbutton(beerFrame, text='Tuborg', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var12,
                     command=tuborg)
tuborg.grid(row=2, column=0, sticky=W)

samuel_adams = Checkbutton(beerFrame, text='SamuelAdams', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                           variable=var13, command=samual_adams)
samuel_adams.grid(row=3, column=0, sticky=W)

indian = Checkbutton(beerFrame, text='India_spl(90)', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var14,
                     command=indian)
indian.grid(row=4, column=0, sticky=W)

bluemoon = Checkbutton(beerFrame, text='BlueMoon', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var15,
                       command=bluemoon)
bluemoon.grid(row=5, column=0, sticky=W)

budweisermagnum = Checkbutton(beerFrame, text='BudweiserMagnum', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                              variable=var16, command=budweisermagnum)
budweisermagnum.grid(row=6, column=0, sticky=W)

budlightlime = Checkbutton(beerFrame, text='BudLightLime', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                           variable=var17, command=budlightlime)
budlightlime.grid(row=7, column=0, sticky=W)


carlsberg = Checkbutton(beerFrame, text='Carlsberg', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var18,
                        command=carlsberg)
carlsberg.grid(row=8, column=0, sticky=W)


# Entry Fields for Beer Items

textoldmonk = Entry(beerFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_oldmonk)
textoldmonk.grid(row=0, column=1)

textkingfisher = Entry(beerFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_kingfisher)
textkingfisher.grid(row=1, column=1)

texttuborg = Entry(beerFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_tuborg)
texttuborg.grid(row=2, column=1)

textsamual_adams = Entry(beerFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_samual_adams)
textsamual_adams.grid(row=3, column=1)

textindian = Entry(beerFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_indian)
textindian.grid(row=4, column=1)

textbluemoon = Entry(beerFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_bluemoon)
textbluemoon.grid(row=5, column=1)

textbudweisermagnum = Entry(beerFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_budweisermagnum)
textbudweisermagnum.grid(row=6, column=1)

textbudlightlime = Entry(beerFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED,
                    textvariable=e_budlightlime)
textbudlightlime.grid(row=7, column=1)

textcarlsberg = Entry(beerFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_carlsberg)
textcarlsberg.grid(row=8, column=1)


# cigarette

marlboro = Checkbutton(cigaretteFrame, text='Marlboro', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                       variable=var19, command=marlboro)
marlboro.grid(row=0, column=0, sticky=W)

total = Checkbutton(cigaretteFrame, text='Total', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var20,
                    command=total)
total.grid(row=1, column=0, sticky=W)

goldflake = Checkbutton(cigaretteFrame, text='GoldFlake', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                        variable=var21, command=goldflake)
goldflake.grid(row=2, column=0, sticky=W)

royal = Checkbutton(cigaretteFrame, text='Royal', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var22,
                    command=royal)
royal.grid(row=3, column=0, sticky=W)

kings = Checkbutton(cigaretteFrame, text='Kings', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var23,
                    command=kings)
kings.grid(row=4, column=0, sticky=W)

scissors = Checkbutton(cigaretteFrame, text='Scissors', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                       variable=var24, command=scissors)
scissors.grid(row=5, column=0, sticky=W)

wills = Checkbutton(cigaretteFrame, text='Wills', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var25,
                    command=wills)
wills.grid(row=6, column=0, sticky=W)

camel = Checkbutton(cigaretteFrame, text='Camel', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=var26,
                    command=camel)
camel.grid(row=7, column=0, sticky=W)

kajabeedi = Checkbutton(cigaretteFrame, text='KajaBeedi', font=('arial', 15, 'bold'), onvalue=1, offvalue=0,
                        variable=var27, command=kajabeedi)
kajabeedi.grid(row=8, column=0, sticky=W)


# Entry Field for Pills Items

textmarlboro = Entry(cigaretteFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_marlboro)
textmarlboro.grid(row=0, column=1)

texttotal = Entry(cigaretteFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_total)
texttotal.grid(row=1, column=1)

textgoldflake = Entry(cigaretteFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED,
                      textvariable=e_goldflake)
textgoldflake.grid(row=2, column=1)

textroyal = Entry(cigaretteFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_royal)
textroyal.grid(row=3, column=1)

textkings = Entry(cigaretteFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_kings)
textkings.grid(row=4, column=1)

textscissors = Entry(cigaretteFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_scissors)
textscissors.grid(row=5, column=1)

textwills = Entry(cigaretteFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_wills)
textwills.grid(row=6, column=1)

textcamel = Entry(cigaretteFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED, textvariable=e_camel)
textcamel.grid(row=7, column=1)

textkajabeedi = Entry(cigaretteFrame, font=('arial', 15, 'bold'), bd=5, width=5, state=DISABLED,
                      textvariable=e_kajabeedi)
textkajabeedi.grid(row=8, column=1)



# CostLabels & entry firlds

labelcostofside_dish = Label(costFrame, text='Cost of Side_Dish', font=('arial', 16, 'bold'), bg='midnight blue',
                             fg='white')
labelcostofside_dish.grid(row=0, column=0)


textcostofside_dish = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                            textvariable=costofside_dishvar)
textcostofside_dish.grid(row=0, column=1, padx=41)


labelcostofbeer = Label(costFrame, text='Cost of Beer', font=('arial', 16, 'bold'), bg='midnight blue', fg='white')
labelcostofbeer.grid(row=1, column=0)

textcostofbeer = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                       textvariable=costofbeervar)
textcostofbeer.grid(row=1, column=1, padx=41)


labelcostofcigarette = Label(costFrame, text='Cost of Cigarette', font=('arial', 16, 'bold'), bg='midnight blue',
                             fg='white')
labelcostofcigarette.grid(row=2, column=0)

textcostofcigarette = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                            textvariable=costofcigarettevar)
textcostofcigarette.grid(row=2, column=1, padx=41)


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