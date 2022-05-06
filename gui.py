from tkinter import *
def main():
    root =Tk();
    root.title('Books')
    root.geometry("600x400")
    def read_data():
        Label(root,text="Book Identification Number",width=30,height=2).grid(row=0)
        Label(root,text="Book Name",width=10,height=2).grid(row=1)
        Label(root,text="Price",width=6,height=2).grid(row=2)
        Label(root,text="Quantity Available",width=19,height=2).grid(row=3)
        Label(root,text="Quantity Sold",width=14,height=2).grid(row=4)
        e1=Entry(root)
        e2=Entry(root)
        e3=Entry(root)
        e4=Entry(root)
        e5=Entry(root)
        e1.grid(row=0,column=1)
        e2.grid(row=1,column=1)
        e3.grid(row=2,column=1)
        e4.grid(row=3,column=1)
        e5.grid(row=4,column=1)
        data={"e1":e1,"e2":e2,"e3":e3,"e4":e4,"e5":e5}
        return data
    def retrieve_data(data):
        bookid=data["e1"].get()
        bookname=data["e2"].get()
        price=data["e3"].get()
        quantityavail=data["e4"].get()
        quantitysold=data["e5"].get()
        fin_data={"Bookid":bookid,"BookName":bookname,"Price":price,"QuantityAvail":quantityavail,"QuantitySold":quantitysold}
        return fin_data
    def submit(data):
        final_data=retrieve_data(data)
        print("Book ID=",final_data["Bookid"])
        print("Book Name=",final_data["BookName"])
        print("Price=",final_data["Price"])
        print("Quantity Available=",final_data["QuantityAvail"])
        print("Quantity Sold=",final_data["QuantitySold"])
    data=read_data()
    Button(root,text="Add Entry",command=lambda:[retrieve_data(data),submit(data)]).grid(row=6,column=3)

    mainloop()
main()