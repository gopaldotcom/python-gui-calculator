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
    
  del_operator()   
    
    current = display_entry.get()   
    
    if current == "":  
        current = '0'
        
  
    left = current.count("(")
    right = current.count(")")
    if left > right:
        for _ in range(left-right):
            current += ")"

    
    last_questestion = current  
    if "%" in current:
        for _ in range(current.count("%")):
            current = current.replace("%", "/100")
            
  
    try:
        if check_safe_for_eval(current):    
            result = eval(current)       
           
            if result == int(result):
                result = int(result)
                
            
            result = round(result, 13) 
           
            
           
            if abs(result - int(round(result))) < 0.000_000_000_001:
                result = int(round(result))
            
            update_input_ready_status(True) 
        else:
            raise ValueError("Unauthorized input")
    
    except:
        def clear_display():
            display_entry.delete(0, END)
            equals_button.config(bg=COLORS[1], fg=COLORS[3], state=NORMAL)
        def error_print():
            display_entry.delete(0, END)
            display_entry.insert(0, "ERROR")
            equals_button.config(bg="red", state=DISABLED)
            window.after(1500, clear_display)   
        window.after(0, error_print)   
        result = "err"  
        
   
    display_entry.delete(0, END)
    display_entry.insert(0, str(result))
    
   
    global Last_Display 
    if "=" in str(Last_Display):   
        Last_Display_result = Last_Display.split('=')[-1]   
    else:
        Last_Display_result = Last_Display  
    Last_Display_2 = Last_Display
    if result == "err":
        Last_Display = (f"{last_questestion}={result}")  
    else:
        Last_Display = (f"{last_questestion}={result:,}") 
    if len(Last_Display) >= 40:
        Last_Display = f"{result:,}"   
    if Last_Display_result != current:  
        if recent_label_1["text"] == "":
            recent_label_1.config(text=Last_Display)
        else:
            recent_label_2.config(text=Last_Display_2)
            recent_label_1.config(text=Last_Display)
            
            
