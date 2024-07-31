import tkinter as tk

calculation=""

def add_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    pass

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,'end')
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")
        

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,'end')

def delete():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


root = tk.Tk()
root.title('Calculator')
root.geometry("330x275")
text_result = tk.Text(root, height=2, width=18, font=("Arial", 24))
text_result.grid(columnspan=6)

btn_1 = tk.Button(root, text='1', width=5, font=('Arial',14),command = lambda: add_calculation(1))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text='2', width=5, font=('Arial',14),command = lambda: add_calculation(2))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text='3', width=5, font=('Arial',14),command = lambda: add_calculation(3))
btn_3.grid(row=2, column=3)
btn_add = tk.Button(root, text='+', width=5, font=('Arial',14),command = lambda: add_calculation('+'))
btn_add.grid(row=2, column=4)
btn_power = tk.Button(root, text='^', width=5, font=('Arial',14),command = lambda: add_calculation('**'))
btn_power.grid(row=2, column=5)

btn_4 = tk.Button(root, text='4', width=5, font=('Arial',14),command = lambda: add_calculation(4))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text='5', width=5, font=('Arial',14),command = lambda: add_calculation(5))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text='6', width=5, font=('Arial',14),command = lambda: add_calculation(6))
btn_6.grid(row=3, column=3)
btn_sub = tk.Button(root, text='-', width=5, font=('Arial',14),command = lambda: add_calculation('-'))
btn_sub.grid(row=3, column=4)
btn_remainder = tk.Button(root, text='Mod', width=5,height=1, font=('Arial',14),command = lambda: add_calculation('%'))
btn_remainder.grid(row=3, column=5)

btn_7 = tk.Button(root, text='7', width=5, font=('Arial',14),command = lambda: add_calculation(7))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text='8', width=5, font=('Arial',14),command = lambda: add_calculation(8))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text='9', width=5, font=('Arial',14),command = lambda: add_calculation(9))
btn_9.grid(row=4, column=3)
btn_mul = tk.Button(root, text='*', width=5, font=('Arial',14),command = lambda: add_calculation('*'))
btn_mul.grid(row=4, column=4)
btn_point = tk.Button(root, text='.', width=5, font=('Arial',14),command = lambda: add_calculation('.'))
btn_point.grid(row=4, column=5)


btn_0 = tk.Button(root, text='0', width=5, font=('Arial',14),command = lambda: add_calculation(0))
btn_0.grid(row=5, column=1)
btn_openParanthasis = tk.Button(root, text='(', width=5, font=('Arial',14),command = lambda: add_calculation('('))
btn_openParanthasis.grid(row=5, column=2)
btn_closedParanthasis = tk.Button(root, text=')', width=5, font=('Arial',14),command = lambda: add_calculation(')'))
btn_closedParanthasis.grid(row=5, column=3)
btn_divide = tk.Button(root, text='/', width=5, font=('Arial',14),command = lambda: add_calculation('/'))
btn_divide.grid(row=5, column=4)
btn_equal = tk.Button(root, text='=', width=5, font=('Arial',14),command = evaluate_calculation)
btn_equal.grid(row=5, column=5)



btn_clear = tk.Button(root, text='Clear', width=5, font=('Arial',14),command = clear_field)
btn_clear.grid(row=6, column=3)
btn_delete = tk.Button(root, text='X', width=5, font=('Arial',14),command = delete)
btn_delete.grid(row=6, column=2)



root.mainloop()