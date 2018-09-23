from tkinter import *
root = Tk()
root.title("Scrollbar Widget")
list = ["Shirt","Bag","Toy","Books","Fruits",
        "Vegetables","Jeans","Headphones",
        "Watch","Dress","Snaks","Dry fruits"]
def add():
    w = Lb.get(ACTIVE)
    cart.insert(END,w)
    Scr.set(100,400)
    print("Item {} Added to Your Cart".format(w))
Lb = Listbox(root)
Lb.pack(side=LEFT, expand=1,fill=X)

cart = Listbox(root)
cart.pack(side=RIGHT, expand=1,fill=X)

Scr = Scrollbar(root,troughcolor='red',jump=1)
Scr.pack(side=LEFT,fill=Y)

Btn= Button(root,text="ADD TO CART ->",fg='white',bg='green',command=add).pack(side=RIGHT)
for i in list:
    Lb.insert(END ,i)

Lb.config(yscrollcommand=Scr.set)
Scr.config(command=Lb.yview)
mainloop()
