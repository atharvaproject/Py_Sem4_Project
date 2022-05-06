import tkinter as tk
from tkinter import *
from booksheet_functions import *
from invoicegen_functions import *

def manageInventory():
    InventoryString = '''Press 1 to add a new book.
    Press 2 to edit an existing book price.
    Press 3 to edit the number of books currently available. 
    Press 4 to delete an existing record. 
    Press 5 to view BIN records.'''
    print(InventoryString)
    dec = input("Enter: ")
    if(dec=='1'):
        bname = input("Enter book title:")
        price = input("Enter book price:")
        qavail = input("Enter quantity available:")
        qsold = input("Enter quantity sold:")
        addBook(bname, price, qavail, qsold)
        print('Book added.')
    elif(dec=='2'):
        bin = input("Enter BIN of book:")
        new = input("Enter new price:")
        editbookprice(bin, new)
        print('Price updated.')
    elif (dec == '3'):
        bin = input("Enter BIN of book:")
        new = input("Enter quantity available:")
        editqavail(bin, new)
        print('Quantity updated.')
    elif (dec == '4'):
        bin = input("Enter BIN of book:")
        delRecord(bin)
        print('Record deleted.')
    elif(dec=='5'):
        dispBIN()
        print('END.')

def InvoiceGenerate():
    cname = input("Enter customer name:")
    pm = input("Enter payment method:")
    bin1 = input("Enter BIN of 1st book:")
    b1qty = input("Enter the units of 1st book bought:")
    b1qty = int(b1qty)
    dispAddBookStr()
    dec2 = input("Enter: ")
    binlist=[]
    bqtylist=[]
    for i in range(0,int(dec2)):
        bin = input("Enter BIN of book:")
        binlist.append(bin)
        bqty = input("Enter the units of book bought:")
        bqtylist.append(int(bqty))
    if(dec2=='0'):
        genInvoice(cname,pm,bin1,b1qty)
    elif(dec2=='1'):
        genInvoice(cname, pm, bin1, b1qty, binlist[0], bqtylist[0])
    elif (dec2 == '2'):
        genInvoice(cname, pm, bin1, b1qty, binlist[0], bqtylist[0], binlist[1], bqtylist[1])
    elif (dec2 == '3'):
        genInvoice(cname, pm, bin1, b1qty, binlist[0], bqtylist[0], binlist[1], bqtylist[1], binlist[2], bqtylist[2])
    elif (dec2 == '4'):
        genInvoice(cname, pm, bin1, b1qty, binlist[0], bqtylist[0], binlist[1], bqtylist[1], binlist[2], bqtylist[2], binlist[3], bqtylist[3])

def dispAddBookStr():
    invstr = ''' Press 0 if no other books have been bought. 
    Else enter the number of additional books bought. '''
    print(invstr)

m = tk.Tk();
m.title('BOOKWORM')
m.geometry("600x400")
btn = Button(m, width=25, text='ADD BOOK', command=manageInventory)
btn.pack()
btn.place(x=200, y=100)
btn2 = Button(m, width=25, text='GENERATE INVOICE', command=InvoiceGenerate)
btn2.pack()
btn2.place(x=200, y=300)
m.mainloop()


