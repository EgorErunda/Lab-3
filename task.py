import tkinter as tk
import random 
import string

window = tk.Tk()
window.geometry('1280x720')
window.resizable(width=False, height=False)
window.title('keygen for Assasins Creed')
window.config(bg='#000000')

#Функция для генерации ключа
def generateKey():
    def generatePart():
        digits = random.sample(string.digits, 2)
        letters = random.sample(string.ascii_letters, 3)
        part = digits + letters
        random.shuffle(part)
        return ''.join(part)

    part1 = generatePart()
    part2 = generatePart()
    part3 = generatePart()

    key = f"{part1}-{part2}-{part3}"
    return key


#Функция для отображения ключа
def displayKey():
  key = generateKey()
  text_field.delete(1, tk.END)
  text_field.insert(tk.END, key)


#Задний фон
window.image = tk.PhotoImage(file='bg_small.png')
bg_logo = tk.Label(window, image= window.image)
bg_logo.place(x=0,y=0)
#Название игры
title_lbl = tk.Label(window,
            text="Assasin`s Creed",
            font = ("Comic Sans MS", 55, 'bold'),
            bg = '#000000',
            fg = '#cc1100')
title_lbl.place(x=70, y=20)
#Кнопка для генерации ключа
btn1 = tk.Button(window,
                 bg='#F3D500',
                 fg='black',
                 text='Получть доступ\n к яблоку Эдема!',
                 font=("Arial", 20, 'bold'),
                 activebackground='red',
                 activeforeground='white',
                 command=lambda: displayKey())
btn1.place(x=310,y=410)
#Поле для вывода ключа
text_field = tk.Entry(window, font=('', 15), width=20)
text_field.place(x=930, y=550)



window.mainloop()