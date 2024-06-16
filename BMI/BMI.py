import tkinter as tk

window = tk.Tk()
window.title('BMI Calculator')
window.iconbitmap('E:\Programming\Python\Python GUI\BMI\BMIcalculator.ico')

window.geometry(f'{400}x{500}+{500}+{100}')
window.configure(bg='#C6C6C6')


def calculate_bmi(w , h):
    if 20 <= w <= 200 and 100 < h < 300:
        bmi = (w/(h*h))*10000

        result = (f'BMI: {round(bmi , 2)}, kg/m²')

        if bmi < 18.5:
            result += ('\nUnderweight')
        elif 18.5 <= bmi <= 24.9:
             result += ('\nNormal weight')
        elif 25.0 <= bmi <= 29.9:
            result += ('\nOverweight')
        elif 30 <= bmi <= 34.9:
            result += ('\nObesity class I')
        elif 35.0 <= bmi <= 39.9:
            result += ('\nObesity class II')
        elif bmi >= 40:
            result += ('\nObesity class III')
    else:
        result = ('Enter valid details.')

    answer.set(result)


def clear_fields():
    number1.set(0)
    number2.set(0)
    number3.set(0)
    answer.set('')

number1 = tk.IntVar()
number2 = tk.IntVar()
number3 = tk.IntVar()
answer = tk.StringVar()
gender = tk.IntVar()

label = tk.Label(
    text='BMI Calculator', bg='#C6C6C6', font=('"Times New Roman", Times, serif' , 35 , "bold")
)
label.pack()


label = tk.Label(
    text='Age(ages: 2 - 120)', bg='#C6C6C6', font=('"Times New Roman", Times, serif' , 15)
)
label.place(x=20 , y=100)
entry = tk.Entry(
    textvariable=number1, bg='white', borderwidth=2, font=('Arial', 20), width=5
)
entry.place(x=200 , y=100)


label = tk.Label(
    text='Gender', bg='#C6C6C6', font=('"Times New Roman", Times, serif' , 15)
)
label.place(x=20 ,y=150)
Radiobutton = tk.Radiobutton(
    text = 'Male',variable=gender ,value = 1, bg='#C6C6C6', font=('"Times New Roman", Times, serif' , 15)
)
Radiobutton.place(x=200 , y=150)

Radiobutton = tk.Radiobutton(
    text = 'Female',variable=gender, value = 2, bg='#C6C6C6', font=('"Times New Roman", Times, serif' , 15)
)
Radiobutton.place(x=280 , y=150)


label = tk.Label(
    text='Height', bg='#C6C6C6', font=('"Times New Roman", Times, serif' , 15)
)
label.place(x=20 ,y=200)
entry = tk.Entry(
    textvariable=number2, bg='white', borderwidth=2, font=('Arial', 20), width=10
)
entry.place(x=200 , y=200)
label = tk.Label(
    text='cm', bg='#C6C6C6', font=('"Times New Roman", Times, serif' , 15 , 'bold')
)
label.place(x=360 ,y=205)


label = tk.Label(
    text='Weight', bg='#C6C6C6', font=('"Times New Roman", Times, serif' , 15)
)
label.place(x=20 ,y=250)
entry = tk.Entry(
    textvariable=number3, bg='white', borderwidth=2, font=('Arial', 20), width=10
)
entry.place(x=200 , y=250)
label = tk.Label(
    text='kg', bg='#C6C6C6', font=('"Times New Roman", Times, serif' , 15 , 'bold')
)
label.place(x=360 ,y=255)

label = tk.Label(
    textvariable=answer, bg='#C6C6C6', fg='red', font=('"Times New Roman", Times, serif' , 20 , 'bold')
)
label.place(x=90, y=320)

button = tk.Button(
    text='Calculate', width=8, height=1, bg='#37C700',font=('"Times New Roman", Times, serif' , 15 , 'bold'),
    command = lambda: calculate_bmi(number3.get(), number2.get() )
)
button.place(x=100, y=400)

button = tk.Button(
    text='Clear', width=5, height=1, bg='#4A4A4A',font=('"Times New Roman", Times, serif' , 15 , 'bold'),
    command= clear_fields
)
button.place(x=240, y=400)



window.mainloop()