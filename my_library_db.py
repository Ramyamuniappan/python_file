#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# UTF - 8 characters used in this this file

try:# for Python2
    from Tkinter import *
    import Tkinter
    import tkSimpleDialog as simpledialog
    import tkMessageBox 
    #from Tkinter import tkMessageBox
    import ttk
except:# for Python3
    from tkinter import *
    import tkinter
    import tkinter as Tkinter
    import tkinter.simpledialog as simpledialog
    import tkinter.messagebox as tkMessageBox
    #from tkinter import messagebox
    import tkinter.ttk as ttk


import sys, csv

home_screen = {    "master":None,\
                "root":None}

db_list = []
button_frames = {"button1":None,"button2":None,"button3":None}
button_objs = {"add":None,"print":None,"exit":None}
button_bgcolor = 'blue'
def get_data_from_db():
    db_list = []
    if len(sys.argv) == 2:
        try:
            with open(sys.argv[1]) as libfile:
                for line in csv.reader(libfile, dialect="excel-tab"):#delimiter="\t"
                    if line:
                        db_list.append(line)
        except Exception as e:
            print (e)
            print ("exitting ...")
            return None 
        else:
            return db_list   
    else:
        print ("Error Usage: python my_lirary_db.py library.txt")
        return None

def insert_data_to_db(db_list):
    try:
        with open(sys.argv[1], mode='w') as lib_file:
            dbhandler = csv.writer(lib_file, dialect="excel-tab", quoting=csv.QUOTE_MINIMAL)#delimiter="\t"
            for line in db_list:
                dbhandler.writerow(line)
    except Exception as e:
        print (e)
        print ("exitting ...")    

def sort_db_list(my_db_list): 
    print (my_db_list)
    my_db_list.sort(key = lambda x: x[1]) 
    return my_db_list

def exit():
    global home_screen;
    home_screen["master"].destroy()

def add():
    global db_list
    book_detail = []
    title = simpledialog.askstring("Input", "BookTitle", parent=home_screen["master"])
    name = simpledialog.askstring("Input", "author_name", parent=home_screen["master"])
    isbn = simpledialog.askstring("Input", "ISBN", parent=home_screen["master"])
    if title == None or title == '':
        title = "NA"
    if name == None or name == '':
        name = "NA"
    if isbn == None or isbn == '':
        isbn = "NA"
    book_detail.append(title)
    book_detail.append(name)
    book_detail.append(isbn)
    if ask_message(str(book_detail)):
        db_list.append(book_detail)
        my_db_list = sort_db_list(db_list)
        print (my_db_list)
        insert_data_to_db(my_db_list)
        
def show_message(message):
    tkMessageBox.showinfo("Your Book details", message)

def ask_message(message):
    return tkMessageBox.askyesno("Save", message)

def prints():
    global db_list
    show_message(str(db_list))

def home_screen_config():
    global home_screen
    home_screen["master"] = Tkinter.Tk()
    Grid.rowconfigure(home_screen["master"], 0, weight=1)
    Grid.columnconfigure(home_screen["master"], 0, weight=1)
    home_screen["master"].geometry('{}x{}'.format(800,480))
    home_screen["root"]=Frame(home_screen["master"], bg='black')
    home_screen["root"].grid(row=0, column=0, sticky=N+S+E+W)
    for x in range(3):
        Grid.rowconfigure(home_screen["root"], x, weight=1)
    for x in range(7):
        Grid.columnconfigure(home_screen["root"], x, weight=1)

def button_config():
    global home_screen, button_frames, button_objs
    button_frames["button1"] = Frame(home_screen["root"], borderwidth=1,  bg='black', relief="solid")
    button_frames["button1"].grid( row=1, column=1, columnspan=1, sticky=N+S+E+W)
    button_frames["button2"] = Frame(home_screen["root"], borderwidth=1,  bg='black', relief="solid")
    button_frames["button2"].grid( row=1, column=3, columnspan=1, sticky=N+S+E+W)
    button_frames["button3"] = Frame(home_screen["root"], borderwidth=1,  bg='black', relief="solid")
    button_frames["button3"].grid( row=1, column=5, columnspan=1, sticky=N+S+E+W)
    button_objs["add"] = Button(button_frames["button1"]) 
    button_objs["add"].config(text = "Add", bg=button_bgcolor, borderwidth=1, fg="white", highlightbackground="white", activebackground='green', bd=0,command=add)
    button_objs["add"].place()
    button_objs["add"].pack(fill = X,padx=(0,0), pady=(0,0), side = 'bottom')
    button_objs["print"] = Button(button_frames["button2"]) 
    button_objs["print"].config(text = "print", bg=button_bgcolor, borderwidth=1, fg="white", highlightbackground="white",activebackground='green', bd=0,command=prints)
    button_objs["print"].place()
    button_objs["print"].pack(fill = X,padx=(0,0), pady=(0,0), side = 'bottom') 
    button_objs["exit"] = Button(button_frames["button3"]) 
    button_objs["exit"].config(text = "exit", bg=button_bgcolor,borderwidth=1, fg="white", highlightbackground="white", activebackground='green', bd=0,command=exit)
    button_objs["exit"].place()
    button_objs["exit"].pack(fill = X,padx=(0,0), pady=(0,0), side = 'bottom') 
    
if __name__ == "__main__":
    db_list = get_data_from_db()
    if db_list:
        home_screen_config()
        button_config()
        home_screen["master"].mainloop()