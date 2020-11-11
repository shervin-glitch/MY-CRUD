#This APP Is Created By Shervin.bdn And YOU CAN COPY IT and USE it in your Works But Fuck U ALL If U Did that XDDDD
#Run It On Pychram Windows
#This is The Windows Version Of App
#So Dont Fuck My App
#But
#My Bros Can Copy IT XDDDD

from tkinter import Tk , Toplevel , Label , Button , Entry , StringVar , RAISED , GROOVE

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

        def select_data(sl):
            if sl=="st":
                code = sv_en01.get()
                name = sv_en02.get()
                family = sv_en03.get()
                phone = sv_en04.get()


        select_lbl01 = Label(select , text = "Code :" , font = ("Times" , 12 , "bold") , bg = "DarkOrange" , fg = "#ffffff")
        select_lbl02 = Label(select , text = "Name :" , font = ("Times" , 12 , "bold") , bg = "DarkOrange" , fg = "#ffffff")
        select_lbl03 = Label(select , text = "Family :" , font = ("Times" , 12 , "bold") , bg = "DarkOrange" , fg = "#ffffff")
        select_lbl04 = Label(select , text = "Phone :" , font = ("Times" , 12 , "bold") , bg = "DarkOrange" , fg = "#ffffff")

        select_lbl01.place(x = 92 , y = 0)
        select_lbl02.place(x = 92 , y = 80)
        select_lbl03.place(x = 92 , y = 160)
        select_lbl04.place(x = 92 , y = 240)

        select_lbl01.config(width = 12 , height = 1)
        select_lbl02.config(width = 12 , height = 1)
        select_lbl03.config(width = 12 , height = 1)
        select_lbl04.config(width = 12 , height = 1)

        sv_en01 = StringVar()
        sv_en02 = StringVar()
        sv_en03 = StringVar()
        sv_en04 = StringVar()

        select_entry01 = Entry(select , textvariable = sv_en01 , relief = GROOVE , justify = "center")
        select_entry02 = Entry(select , textvariable = sv_en02 , relief = GROOVE , justify = "center")
        select_entry03 = Entry(select , textvariable = sv_en03 , relief = GROOVE , justify = "center")
        select_entry04 = Entry(select , textvariable = sv_en04 , relief = GROOVE , justify = "center")

        select_entry01.place(x = 25 , y = 33)
        select_entry02.place(x = 25 , y = 110)
        select_entry03.place(x = 25 , y = 190)
        select_entry04.place(x = 25 , y = 270)

        select_entry01.config(width = 40)
        select_entry02.config(width = 40)
        select_entry03.config(width = 40)
        select_entry04.config(width = 40)

        btn_select = Button(select , text = "Select Data" , command = lambda : select_data("st") , font = ("Times" , 10 , "bold") , bg = "DarkOrange" , fg = "#ffffff" , relief = RAISED , borderwidth = 5)
        btn_select.place(x = 88 , y = 320)
        btn_select.config(width = 15 , height = 2)

        select.mainloop()
    elif btn=="03":
        update = Toplevel()
        update.title("Update Data")
        update.geometry("300x500")
        update.resizable(0 , 0)
        update.config(background = "Pink")

        def update_data(up):
            if up=="ut":
                code = sv_en01.get()
                name = sv_en02.get()
                family = sv_en03.get()
                phone = sv_en04.get()


        update_lbl01 = Label(update , text = "Code :" , font = ("Times" , 12 , "bold") , bg = "DeepPink" , fg = "#ffffff")
        update_lbl02 = Label(update , text = "Name :" , font = ("Times" , 12 , "bold") , bg = "DeepPink" , fg = "#ffffff")
        update_lbl03 = Label(update , text = "Family :" , font = ("Times" , 12 , "bold") , bg = "DeepPink" , fg = "#ffffff")
        update_lbl04 = Label(update , text = "Phone :" , font = ("Times" , 12 , "bold") , bg = "DeepPink" , fg = "#ffffff")

        update_lbl01.place(x = 92 , y = 0)
        update_lbl02.place(x = 92 , y = 80)
        update_lbl03.place(x = 92 , y = 160)
        update_lbl04.place(x = 92 , y = 240)

        update_lbl01.config(width = 12 , height = 1)
        update_lbl02.config(width = 12 , height = 1)
        update_lbl03.config(width = 12 , height = 1)
        update_lbl04.config(width = 12 , height = 1)

        sv_en01 = StringVar()
        sv_en02 = StringVar()
        sv_en03 = StringVar()
        sv_en04 = StringVar()

        update_entry01 = Entry(update , textvariable = sv_en01 , relief = GROOVE , justify = "center")
        update_entry02 = Entry(update , textvariable = sv_en02 , relief = GROOVE , justify = "center")
        update_entry03 = Entry(update , textvariable = sv_en03 , relief = GROOVE , justify = "center")
        update_entry04 = Entry(update , textvariable = sv_en04 , relief = GROOVE , justify = "center")

        update_entry01.place(x = 25 , y = 33)
        update_entry02.place(x = 25 , y = 110)
        update_entry03.place(x = 25 , y = 190)
        update_entry04.place(x = 25 , y = 270)

        update_entry01.config(width = 40)
        update_entry02.config(width = 40)
        update_entry03.config(width = 40)
        update_entry04.config(width = 40)

        btn_update = Button(update , text = "Update Data" , command = lambda : update_data("ut") , font = ("Times" , 10 , "bold") , bg = "DeepPink" , fg = "#ffffff" , relief = RAISED , borderwidth = 5)
        btn_update.place(x = 88 , y = 320)
        btn_update.config(width = 15 , height = 2)

        update.mainloop()
    elif btn=="04":
        delete = Toplevel()
        delete.title("Delete Data")
        delete.geometry("300x500")
        delete.resizable(0 , 0)
        delete.config(background = "Red")

        def delete_data(dl):
            if dl=="dt":
                code = sv_en01.get()
                name = sv_en02.get()
                family = sv_en03.get()
                phone = sv_en04.get()


        delete_lbl01 = Label(delete , text = "Code :" , font = ("Times" , 12 , "bold") , bg = "DarkRed" , fg = "#ffffff")
        delete_lbl02 = Label(delete , text = "Name :" , font = ("Times" , 12 , "bold") , bg = "DarkRed" , fg = "#ffffff")
        delete_lbl03 = Label(delete , text = "Family :" , font = ("Times" , 12 , "bold") , bg = "DarkRed" , fg = "#ffffff")
        delete_lbl04 = Label(delete , text = "Phone :" , font = ("Times" , 12 , "bold") , bg = "DarkRed" , fg = "#ffffff")

        delete_lbl01.place(x = 92 , y = 0)
        delete_lbl02.place(x = 92 , y = 80)
        delete_lbl03.place(x = 92 , y = 160)
        delete_lbl04.place(x = 92 , y = 240)

        delete_lbl01.config(width = 12 , height = 1)
        delete_lbl02.config(width = 12 , height = 1)
        delete_lbl03.config(width = 12 , height = 1)
        delete_lbl04.config(width = 12 , height = 1)

        sv_en01 = StringVar()
        sv_en02 = StringVar()
        sv_en03 = StringVar()
        sv_en04 = StringVar()

        delete_entry01 = Entry(delete , textvariable = sv_en01 , relief = GROOVE , justify = "center")
        delete_entry02 = Entry(delete , textvariable = sv_en02 , relief = GROOVE , justify = "center")
        delete_entry03 = Entry(delete , textvariable = sv_en03 , relief = GROOVE , justify = "center")
        delete_entry04 = Entry(delete , textvariable = sv_en04 , relief = GROOVE , justify = "center")

        delete_entry01.place(x = 25 , y = 33)
        delete_entry02.place(x = 25 , y = 110)
        delete_entry03.place(x = 25 , y = 190)
        delete_entry04.place(x = 25 , y = 270)

        delete_entry01.config(width = 40)
        delete_entry02.config(width = 40)
        delete_entry03.config(width = 40)
        delete_entry04.config(width = 40)

        btn_delete = Button(delete , text = "Delete Data" , command = lambda : delete_data("dt") , font = ("Times" , 10 , "bold") , bg = "DarkRed" , fg = "#ffffff" , relief = RAISED , borderwidth = 5)
        btn_delete.place(x = 88 , y = 320)
        btn_delete.config(width = 15 , height = 2)

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