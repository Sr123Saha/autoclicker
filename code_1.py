# the place where the program is located
# здесь находится код программы 

import pyautogui as auto
import keyboard as key
from tkinter import *

def start_autoclicker():
    start_key = start_key_entry.get()
    stop_key = stop_key_entry.get()
    pause_key = pause_key_entry.get()
    always_key = always_key_entry.get()
    button_name = button_name_entry.get()
    
    def click1():
        while True:
            if key.is_pressed(start_key):
                auto.tripleClick(button=button_name)
            
            if key.is_pressed(stop_key):
                break
            
            if key.is_pressed(always_key):
                always_click()

    def always_click():
        while True:
            auto.tripleClick(button=button_name)

            if key.is_pressed(pause_key):
                click1()
            
            if key.is_pressed(stop_key):
                break

    # Запуск основной функции
    click1()

root = Tk()
root.title('Автокликер')
root.geometry("400x400")
root.iconbitmap('212.ico')

Label(root, text="выберите клавишу запуска:").pack()
start_key_entry = Entry(root)
start_key_entry.pack()

Label(root, text="выберите клавишу остановки:").pack()
stop_key_entry = Entry(root)
stop_key_entry.pack()

Label(root, text="клавиша для установки паузы:").pack()
pause_key_entry = Entry(root)
pause_key_entry.pack()

Label(root, text="клавиша для клика постояного (то есть если уйти он будет кликать):").pack()
always_key_entry = Entry(root)
always_key_entry.pack()

Label(root, text="какая клавиша мыши кликать будет надо написать (right / left):").pack()
button_name_entry = Entry(root)
button_name_entry.pack()

Button(root, text="Запуск", command=start_autoclicker).pack()

root.mainloop()
