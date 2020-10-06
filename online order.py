from tkinter import *
from tkinter import messagebox
l=Tk()
l.geometry("500x400")
l.title("checking availability")
l.config(bg="black")
Label(text="Product").grid(row=0,column=0)
Product=Entry()
Product.grid(row=0,column=1)
Label(text="count").grid(row=1,column=0)
count=Entry()
count.grid(row=1,column=1)
def check():
    s=Product.get()
    b=count.get()
    f=open("product details.txt","r")
    for i in f:
        if(i.split(" ")[0]==s and b<=i.split(" ")[1]):
            messagebox.showinfo("check","your product is available for purchase")
            break
    else:
        messagebox.showinfo("check","Out of Stock")
    f.close()
Button(text="check",command=check).grid(row=2,column=0,columnspan=2)
l.mainloop()
