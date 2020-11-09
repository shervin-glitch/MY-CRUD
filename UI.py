from tkinter import Tk , Toplevel , Label , Button , Entry , StringVar , RAISED , FLAT , GROOVE

#WINDOW_SETTINGS
root = Tk()
root.geometry("219x290")
root.title("CRUD")
root.resizable(0 , 0)
root.config(background = "LightBlue")

#MAIN_BTN_FUNCTION
def press(btn):
    if btn=="01":
        create = Toplevel()
        create.title("Create Data")
        create.geometry("300x500")
        create.resizable(0 , 0)
        create.config(background = "Green")

        def create_data(cr):
            if cr=="cd":
                code = sv_en01.get()
                name = sv_en02.get()
                family = sv_en03.get()
                phone = sv_en04.get()


        create_lbl01 = Label(create , text = "Code :" , font = ("Times" , 12 , "bold") , bg = "DarkGreen" , fg = "#ffffff")
        create_lbl02 = Label(create , text = "Name :" , font = ("Times" , 12 , "bold") , bg = "DarkGreen" , fg = "#ffffff")
        create_lbl03 = Label(create , text = "Family :" , font = ("Times" , 12 , "bold") , bg = "DarkGreen" , fg = "#ffffff")
        create_lbl04 = Label(create , text = "Phone :" , font = ("Times" , 12 , "bold") , bg = "DarkGreen" , fg = "#ffffff")

        create_lbl01.place(x = 92 , y = 0)
        create_lbl02.place(x = 92 , y = 80)
        create_lbl03.place(x = 92 , y = 160)
        create_lbl04.place(x = 92 , y = 240)

        create_lbl01.config(width = 12 , height = 1)
        create_lbl02.config(width = 12 , height = 1)
        create_lbl03.config(width = 12 , height = 1)
        create_lbl04.config(width = 12 , height = 1)

        sv_en01 = StringVar()
        sv_en02 = StringVar()
        sv_en03 = StringVar()
        sv_en04 = StringVar()

        create_entry01 = Entry(create , textvariable = sv_en01 , relief = GROOVE , justify = "center")
        create_entry02 = Entry(create , textvariable = sv_en02 , relief = GROOVE , justify = "center")
        create_entry03 = Entry(create , textvariable = sv_en03 , relief = GROOVE , justify = "center")
        create_entry04 = Entry(create , textvariable = sv_en04 , relief = GROOVE , justify = "center")

        create_entry01.place(x = 25 , y = 33)
        create_entry02.place(x = 25 , y = 110)
        create_entry03.place(x = 25 , y = 190)
        create_entry04.place(x = 25 , y = 270)

        create_entry01.config(width = 40)
        create_entry02.config(width = 40)
        create_entry03.config(width = 40)
        create_entry04.config(width = 40)

        btn_create = Button(create , text = "Create Data" , command = lambda : create_data("cd") , font = ("Times" , 10 , "bold") , bg = "DarkGreen" , fg = "#ffffff" , relief = RAISED , borderwidth = 5)
        btn_create.place(x = 88 , y = 320)
        btn_create.config(width = 15 , height = 2)

        create.mainloop()
    elif btn=="02":
        select = Toplevel()
        select.title("Select Data")
        select.geometry("300x500")
        select.resizable(0 , 0)
        select.config(background = "Orange")
        select.mainloop()
    elif btn=="03":
        update = Toplevel()
        update.title("Update Data")
        update.geometry("300x500")
        update.resizable(0 , 0)
        update.config(background = "Pink")
        update.mainloop()
    elif btn=="04":
        delete = Toplevel()
        delete.title("Delete Data")
        delete.geometry("300x500")
        delete.resizable(0 , 0)
        delete.config(background = "Red")
        delete.mainloop()

#BTN_CREATE
btn01 = Button(root , text = "Create" , command = lambda : press("01"), font = ("Courier" , 10 , "bold") , bg = "DarkGreen" , fg = "#ffffff" , relief = RAISED , borderwidth = 5)
btn01.place(x = 40 , y = 10)
btn01.config(width = 15 , height = 2)

#BTN_SELECT
btn02 = Button(root , text = "Select" , command = lambda : press("02"), font = ("Courier" , 10 , "bold") , bg = "Orange" , fg = "#ffffff" , relief = RAISED , borderwidth = 5)
btn02.place(x = 40 , y = 80)
btn02.config(width = 15 , height = 2)

#BTN_UPDATE
btn03 = Button(root , text = "Update" , command = lambda : press("03"), font = ("Courier" , 10 , "bold") , bg = "Pink" , fg = "#ffffff" , relief = RAISED , borderwidth = 5)
btn03.place(x = 40 , y = 160)
btn03.config(width = 15 , height = 2)

#BTN_DELETE
btn04 = Button(root , text = "Delete" , command = lambda : press("04"), font = ("Courier" , 10 , "bold") , bg = "Red" , fg = "#ffffff" , relief = RAISED , borderwidth = 5)
btn04.place(x = 40 , y = 230)
btn04.config(width = 15 , height = 2)

root.mainloop()