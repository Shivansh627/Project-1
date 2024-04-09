from tkinter import *
import csv
from tkinter import ttk
from tkcalendar import DateEntry



#show Income

    
def showincome():
    user_input = inco.get()

    if user_input != "" and user_input is not None:
        show.insert("", "end", values=(f"₹{user_input}",))

        data = [user_input]
        with open(r"income.csv", mode="a+", newline='') as cs:
            writer = csv.writer(cs)
            writer.writerow(data)

        read_csv_into_tree(show, r"income.csv")
    
    inco.delete(0, END)

# Add this function to read CSV into Treeview
def read_csv_into_tree(treeview, csv_file):
    treeview.delete(*treeview.get_children())
    with open(csv_file, mode="r") as cs:
        reader = csv.reader(cs)
        for row in reader:
            treeview.insert("", "end", values=row)


#add expense

def addexpense():
    u1 = category_var.get()
    u2 = exp.get()
    u3 = cal.get()

    if u2 != "" and u2 is not None:
        data = [u1, u3, u2]
        with open("data.csv", mode="a+", newline='') as cs:
            write = csv.writer(cs)
            write.writerow(data)

    exp.delete(0, END)
   
#show expense
def showexpense():
    read_csv_into_tree(tree, r"data.csv")
   

#total income
def totex():
    expense.delete(0, 'end')
    with open(r"data.csv",mode="r")as file:
        reader=csv.reader(file)
        expenses = [float(row[2]) for row in reader]

    total_expense = sum(expenses)
    expense.insert("end",total_expense)

# TOTAL INCOME
def totin():
    income.delete(0,'end')
    with open(r"income.csv",mode="r")as file:
        reader=csv.reader(file)
        expenses = [float(row[0]) for row in reader]

    total_expense = sum(expenses)
    income.insert("end",total_expense)




#window
root=Tk()
root.title("EXPENSENSIBLE")
root.geometry("680x610")
root.configure(bg="#CDEAC0")
frame=Frame(root)
frame.pack()

# logo
label=Label(root,text="EXPENSENSIBLE",font=("bold",30),background="#CDEAC0")
label.pack()

# label and inputs
label1=Label(root,text="INCOME",font=("bold",24),bg="#CDEAC0")
label1.place(x=100,y=70)
label2=Label(root,text="EXPENSE",font=("bold",24),bg="#CDEAC0")
label2.place(x=270,y=70)

income=Listbox(root,font="arial 28",width=7,height=1,bg="#CDEAC0")
income.place(x=100,y=110)

expense=Listbox(root,font="arial 28",width=7,height=1,bg="#CDEAC0")
expense.place(x=270,y=110)


# dropdown and entries
label3=Label(root,text="Categories",font=("bold"),bg="#CDEAC0")
label3.place(x=90,y=240)
label4=Label(root,text="Money Out",font=("bold"),bg="#CDEAC0")
label4.place(x=250,y=240)
label5=Label(root,text="Money In",font=("bold"),bg="#CDEAC0")
label5.place(x=110,y=200)
expense_categories = [
    "Tuition and Fees",
    "Books and Supplies",
    
    "Food and Groceries",
    "Transportation",
    "Healthcare",
    
    "Entertainment and Recreation",
    
    "School Supplies",
    
    "Travel and Commuting",
    "Other"
]
category_var = StringVar(root)
category_var.set(expense_categories[0])

category_dropdown = OptionMenu(root, category_var,*expense_categories)
category_dropdown.configure(bg="#CDEAC0")
category_dropdown.place(x=80,y=270)

inc=IntVar()
inco=Entry(root,textvariable=inc,bg="#CDEAC0",width=7,font="arial 18")
inco.place(x=200,y=200)

ex=IntVar()
exp=Entry(root,textvariable=ex,bg="#CDEAC0",width=7,font="arial 18")
exp.place(x=250,y=270)

cal = DateEntry(root, width=12,height=8, background="#CDEAC0", foreground="black", borderwidth=1, date_pattern="y-mm-dd")
cal.place(x=350,y=270)

# buttons
button1 = Button(root, text="Show Income", command=showincome , bg="#CDEAC0")
button1.place(x=100,y=310)

button = Button(root, text="Add Expense", command=addexpense , bg="#CDEAC0")
button.place(x=199,y=310)

button = Button(root, text="Show Expense", command=showexpense , bg="#CDEAC0")
button.place(x=299,y=310)

button = Button(root, text="TOTAL EXPENSE", command=totex , bg="#CDEAC0")
button.place(x=397,y=310)

button = Button(root, text="TOTAL INCOME", command=totin , bg="#CDEAC0")
button.place(x=505,y=310)

# listbox and tree view
show = ttk.Treeview(root, columns=("Income"), show="headings", height=11)
show.heading("Income", text="Income")
show.place(x=70, y=340)


columns = ["Categories", "Date", "Expense"]
style = ttk.Style()
style.configure("Treeview", background="#CDEAC0")

tree = ttk.Treeview(root, height=11, columns=columns, show="headings", style="Treeview")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.place(x=300,y=340)

with open(r"income.csv",mode="r+")as file:
    read=csv.reader(file)

    for row in read:
        show.insert("", "end", values=row)

with open(r"data.csv",mode="r+")as file:
    reader=csv.reader(file)
    expenses = [float(row[2]) for row in reader]

    total_expense = sum(expenses)
    expense.insert("end",total_expense)


with open(r"income.csv",mode="r+")as file:
    reader=csv.reader(file)
    expenses = [float(row[0]) for row in reader]

    total_expense = sum(expenses)
    income.insert("end",total_expense)
root.mainloop()
