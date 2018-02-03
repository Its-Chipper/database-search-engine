from tkinter import *

master = Tk()
master.geometry("135x105")



def buttons():
    global f
    file = open("names.txt","r")
    f = file.read()
    file.close()
    global Badd
    global Bdelete
    global Bsearch
    Badd.configure(text="Add Entry", command=Add)
    Bdelete.configure(text="Delete Entry", command=Delete)
    Bsearch.configure(text="Search", command=Search)
    Bedit.configure(text="Edit", command=Edit)




def Add():
    global StudentInfo
    NameOfStudent = input("What is the name of the student? ").capitalize()
    while True:
        check = 0
        x=0
        try:
            StudentD = int(input("What is the students day of birth? DD "))
            x=1
        except ValueError:
            print("Sorry that wasn't a number")
            check = 1
        if StudentD < 1 or StudentD >31 and check == 0:
            print("Sorry that is an invalid day")
        elif x == 1:
            break
        
    while True:
        check = 0
        x=0
        try:
            StudentO = int(input("What is the students month of birth? MM "))
            x=1
        except ValueError:
            print("Sorry that wasn't a number")
            check = 1
        if StudentO < 1 or StudentO >12 and check == 0:
            print("Sorry that is an invalid month")
        elif x == 1:
            break
        
    while True:
        check = 0
        x=0
        try:
            StudentB = int(input("What is the students year of birth? YYYY "))
            x=1
        except ValueError:
            print("Sorry that wasn't a number")
            check = 1
        if StudentB < 1900 or StudentB >2017 and check == 0:
            print("Sorry that is an invalid year it has to be between 1900 and 2017")
        elif x == 1:
            break
        
    while True:
        check = 0
        x=0
        VE = 0
        y = 0
        try:
            StudentID = int(input("What is the students ID?"))
            x = 1
        except ValueError:
            VE = 1
            print("Sorry that wasn't a number")
            check = 1
        fspl = f.split("\n")
        for info in fspl:
            infospl = info.split(":")
            ID = int(infospl[2])
            if ID == StudentID and VE == 0:
                y = 1
                print("sorry that ID already exists")
        if x == 1 and y != 1:
            break

        
    print("\n{}:{}/{}/{}:{}".format(NameOfStudent,StudentD,StudentO,StudentB,StudentID ))
    StudentInfo = ("{}:{}/{}/{}:{}".format(NameOfStudent,StudentD,StudentO,StudentB,StudentID ))
    print("Is this correct\n")
    Bedit.pack_forget()
    Badd.configure(text="Yes", command=YAdd)
    Bdelete.configure(text="No", command=Add)
    Bsearch.configure(text="Back to start", command=Back)
    
def YAdd():
    F = open("names.txt","r")
    FOpen = F.read()
    FOpen = FOpen.split("\n")
    FOpen.append(StudentInfo)
    FOpen = "\n".join(FOpen)
    file2 = open("names.txt","w")
    file2.write(FOpen)
    file2.close()
    print("Added")
    Back()




    
def Delete():
    Bedit.pack_forget()
    Badd.configure(text = "Display list of ID's", command = listnames)
    Bdelete.configure(text = "Search by ID", command = DeleteItem)
    Bsearch.configure(text = "Back", command = Back)

def DeleteItem():
    global Item
    Fname = 0
    Sname = input("Please enter ID")
    fspl = f.split("\n")
    for names in fspl:
        names = names.split(":")
        if Sname == names[2]:
            names = ":".join(names)
            print(names)
            Fname = 1
            Item = fspl.index(names)
            print("Would you like to delete this entry")
            Badd.configure(text="Yes", command=Ydel)
            Bdelete.configure(text="No", command=Delete)
            Bsearch.configure(text="Back to start", command=Back)
            
    if Fname == 0:
        print("Sorry we don't have that in our database")    

def Ydel():
    fspl = f.split("\n")
    del fspl[Item]
    fspl = "\n".join(fspl)
    file2 = open("names.txt","w")
    file2.write(fspl)
    file2.close()
    print("Deleted")
    Back()
    



def Search():
    Badd.configure(text = "Display list of ID's", command = listnames)
    Bdelete.configure(text = "Search by name", command = searchname)
    Bsearch.configure(text = "Search by ID", command = searchID)
    Bedit.configure(text = "Back", command = buttons)

def listnames():
    fspl = f.split("\n")
    for names in fspl:
        names = names.split(":")
        print("{}:{}".format(names[0],names[2]))
        

def searchname():
    Fname = 0
    Sname = input("Please enter a name")
    fspl = f.split("\n")
    for names in fspl:
        names = names.split(":")
        if Sname.capitalize() == names[0].capitalize():
            ":".join(names)
            print(names)
            Fname = 1
    if Fname == 0:
        print("Sorry we don't have that in our database")

def searchID():
    Fname = 0
    Sname = input("Please enter the ID")
    fspl = f.split("\n")
    for names in fspl:
        names = names.split(":")
        if Sname == names[2]:
            ":".join(names)
            print(names)
            Fname = 1
    if Fname == 0:
        print("Sorry we don't have that in our database")




def Edit():
    Bedit.pack_forget()
    Badd.configure(text = "Display list of ID's", command = listnames)
    Bdelete.configure(text = "Search by ID", command = EditItem)
    Bsearch.configure(text = "Back", command = Back)

def EditItem():
    global IDI
    global Index
    global C
    C = 0
    Fname = 0
    fspl = f.split("\n")
    while True:
        try:
            IDI = int(input("What is the students ID?"))
            break
        except ValueError:
            print("Sorry that wasn't a number")
    for name in fspl:
        names = name.split(":")
        if IDI == int(names[2]):
            Index = fspl.index(name)
            Badd.configure(text = "Change name", command = Cname)
            Bdelete.configure(text = "Change date of birth", command = CDOB)
            Bsearch.configure(text = "Change ID", command = CID)
            Fname = 1
            print(fspl[Index])
    if Fname == 0:
        print("Sorry we don't have that in our database")

def Cname():
    global Changed
    Changed = input("What is the new name? ").capitalize()
    print(Changed)
    C = 0
    print("Is this correct \n")
    Badd.configure(text="Yes", command=YC)
    Bdelete.configure(text="No", command=Cname)
    Bsearch.configure(text="Back to start", command=Back) 
    
def YCname():
    fspl = f.split("\n")
    for names in fspl:
        names = names.split(":")
        if IDI == int(names[2]):
            names[0] = ChangedName.capitalize()
            print(names)
            print("The name has been changed")
            fspl[Index] = ":".join(names)
            fspl = "\n".join(fspl)
            file2 = open("names.txt","w")
            file2.write(fspl)
            file2.close()
    Back()
            
            

            
def CDOB():
    global Changed
    global C
    C = 1 
    while True:
        check = 0
        x=0
        try:
            StudentD = int(input("What is the students day of birth? DD "))
            x=1
        except ValueError:
            print("Sorry that wasn't a number")
            check = 1
        if StudentD < 1 or StudentD >31 and check == 0:
            print("Sorry that is an invalid day")
        elif x == 1:
            break
        
    while True:
        check = 0
        x=0
        try:
            StudentO = int(input("What is the students month of birth? MM "))
            x=1
        except ValueError:
            print("Sorry that wasn't a number")
            check = 1
        if StudentO < 1 or StudentO >12 and check == 0:
            print("Sorry that is an invalid month")
        elif x == 1:
            break
        
    while True:
        check = 0
        x=0
        try:
            StudentB = int(input("What is the students year of birth? YYYY "))
            x=1
        except ValueError:
            print("Sorry that wasn't a number")
            check = 1
        if StudentB < 1900 or StudentB >2017 and check == 0:
            print("Sorry that is an invalid year it has to be between 1900 and 2017")
        elif x == 1:
            break
    Changed = "{}/{}/{}".format(StudentD,StudentO,StudentB)
    print(Changed)
    print("Is this correct \n")
    Badd.configure(text="Yes", command=YC)
    Bdelete.configure(text="No", command=CDOB)
    Bsearch.configure(text="Back to start", command=Back)

def YC():
    fspl = f.split("\n")
    for names in fspl:
        names = names.split(":")
        if IDI == int(names[2]):
            names[C] = str(Changed)
            print(names)
            print("The date of birth has been changed")
            fspl[Index] = ":".join(names)
            fspl = "\n".join(fspl)
            file2 = open("names.txt","w")
            print(fspl)
            file2.write(fspl)
            file2.close()
    Back()
    

def CID():
    global Changed
    global C
    C = 2
    while True:
        check = 0
        x=0
        y = 0
        try:
            Changed = int(input("What is the students ID?"))
            x = 1
        except ValueError:
            print("Sorry that wasn't a number")
            check = 1
        fspl = f.split("\n")
        for info in fspl:
            infospl = info.split(":")
            ID = int(infospl[2])
            if ID == Changed:
                y = 1
                print("sorry that ID already exists")
        if x == 1 and y != 1:
            break
    print(Changed)
    print("Is this correct \n")
    Badd.configure(text="Yes", command=YC)
    Bdelete.configure(text="No", command=CID)
    Bsearch.configure(text="Back to start", command=Back)




def Back():
    global Bedit
    Bedit = Button(master, text="Edit", command=Edit,width=105)
    Bedit.pack()
    buttons()
    


Badd = Button(master, text="Add Entry", command=Add,width=105)
Bdelete = Button(master, text="Delete Entry", command=Delete,width=105)
Bsearch = Button(master, text="Search", command=Search,width=105)
Bedit = Button(master, text="Edit", command=Edit,width=105)

Badd.pack()
Bdelete.pack()
Bsearch.pack()
Bedit.pack()

buttons()
