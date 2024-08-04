from tkinter import *

OPS = ["*", "/", "+", "-"]
BUTTON_FONT = "Courier", 25, "bold"
DISPLAY_FONT = "Courier", 14, "italic"
COLORS = ["#2C3333", "#395B64", "#A5C9CA", "#E7F6F2"]  
ALLOWED_CHARS =list("0123456789./-+*%()")

Last_Display = ""
Prepare_for_New_input = False   


def check_safe_for_eval(user_input):  
    for char in user_input:
        if char not in ALLOWED_CHARS:
            return False 
    return True

def find_last_ops_index(user_input):    
    last_ops_index = 0
    chars = list("/-+*&()")
    replace = list(user_input)
    for c in replace:
        if c in chars:
            if replace.index(c) > last_ops_index:
                last_ops_index = replace.index(c)
                replace[replace.index(c)] = "removed"
    return last_ops_index

def update_input_ready_status(func=False):    
    global Prepare_for_New_input   
    if func == True:
        Prepare_for_New_input = True
    else:
        Prepare_for_New_input = False 
        
def del_operator():    
    current = display_entry.get()
    if len(current) > 0:
        if current[-1] in OPS:
            last_index = len(current) -1
            display_entry.delete(last_index, END)    
                
                



def insert_multiplication():   
    current = display_entry.get()
    if current != "":
        if current[-1] == ")":
            display_entry.insert(END, "*")
            
def number_input(num):
    insert_multiplication() 
    if Prepare_for_New_input == True:
        display_entry.delete(0, END)      
    update_input_ready_status()   
    display_entry.insert(END, num)
    
def operator_button(operator):
    del_operator()
    update_input_ready_status()
    display_entry.insert(END, operator)
    
    


def point():
    update_input_ready_status()
    display_entry.insert(END, ".")
def clear():
    update_input_ready_status()
    display_entry.delete(0, END)
    
    
   
def signchange():
    update_input_ready_status()
    current = display_entry.get()
    last_index = find_last_ops_index(current)    
    if len(current) > 0 and len(current)-1 != last_index and last_index > 0:      
        if last_index > 0:
            if current[last_index] == "*":
                display_entry.insert(last_index + 1, "(-")
            elif current[last_index] == "-":
                display_entry.delete(last_index)
                display_entry.insert(last_index, "+")
            elif current[last_index] == "+":
                display_entry.delete(last_index)
                display_entry.insert(last_index, "-")   
            elif current[last_index] == "(":
                display_entry.insert(last_index + 1, "-")
    elif len(current)-1 == last_index and last_index > 0:
        if current[last_index] == "-":
            display_entry.delete(last_index)
            display_entry.insert(last_index, "+")
        elif current[last_index] == "(":
            display_entry.insert(last_index + 1, "-")    
        else:
            display_entry.delete(last_index)
            display_entry.insert(last_index, "-")                                  
    else:
        if current[0] != "-":
            display_entry.insert(0, "-")
        elif current[0] == "-":
            display_entry.delete(0)      
            
def parentheses():             
    update_input_ready_status()
    current = display_entry.get()
    left = current.count("(")
    right = current.count(")")
    if current == "":
        display_entry.insert(END, "(")
    elif current[-1] == "(":
        display_entry.insert(END, "(")
    elif current[-1] in OPS:
        display_entry.insert(END, "(")
    elif left > right:
        display_entry.insert(END, ")")
    elif left == right:
        if current[-1] in OPS:    
            display_entry.insert(END, "(")    
        else:
            display_entry.insert(END, "*(")    
    else:
        display_entry.insert(END, "error")
        
def equals():
    
