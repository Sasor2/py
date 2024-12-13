import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import random
import statistics
import math

def lab1_function():
    laba1 = "hello, world"
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, laba1)

def lab2_function():
    one = 67
    two = 4
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Сумма = {one + two}\n")
    output_text.insert(tk.END, f"Разность = {one - two}\n")
    output_text.insert(tk.END, f"Умножение = {one * two}\n")
    if two != 0:
        output_text.insert(tk.END, f"Деление = {one / two}\n")
    else:
        output_text.insert(tk.END, "Деление на ноль невозможно\n")
    output_text.insert(tk.END, f"Степень = {one ** two}\n")
    output_text.insert(tk.END, f"Сочетания = {math.comb(one, two)}\n")

def lab3_function():
    rand = [random.randint(1, 99) for _ in range(10)]
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Случайные числа: {rand}\n")
    rand.sort()
    output_text.insert(tk.END, f"Отсортированные: {rand}\n")
    output_text.insert(tk.END, f"Макс: {max(rand)}, Мин: {min(rand)}\n")
    output_text.insert(tk.END, f"Сумма: {sum(rand)}\n")

def lab4_function():
    file_path = askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'a', encoding='utf-8') as f:
            data = [random.randint(1, 99) for _ in range(10)]
            f.write(f"{data}\n")
            average = statistics.mean(data)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Сохраненные данные: {data}\n")
        output_text.insert(tk.END, f"Среднее: {average}\n")

def lab5_function():
    class Dog:
        def __init__(self, name):
            self.name = name
        def bark(self):
            return f"{self.name} говорит: Гав-гав!"

    class Cat(Dog):
        def meow(self):
            return f"{self.name} говорит: Мяу!"

    dog = Dog("Шарик")
    cat = Cat("Мурка")

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, dog.bark() + "\n")
    output_text.insert(tk.END, cat.bark() + "\n")
    output_text.insert(tk.END, cat.meow() + "\n")

root = tk.Tk()
root.title("Лабораторная работа")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="Лабораторные работы Шаталова", font=("Arial", 18), bg="#f0f0f0")
title_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

buttons = [
    ("Лаба 1", lab1_function),
    ("Лаба 2", lab2_function),
    ("Лаба 3", lab3_function),
    ("Лаба 4", lab4_function),
    ("Лаба 5", lab5_function)
]

for text, command in buttons:
    btn = ttk.Button(button_frame, text=text, command=command)
    btn.pack(side=tk.LEFT, padx=10, pady=5)

output_frame = tk.Frame(root, bg="#f0f0f0")
output_frame.pack(pady=10)

output_label = tk.Label(output_frame, text="Результат:", font=("Arial", 14), bg="#f0f0f0")
output_label.pack(anchor="w")

output_text = tk.Text(output_frame, height=20, width=80, wrap=tk.WORD, font=("Courier New", 12), borderwidth=2, relief="solid")
output_text.pack(pady=5)

root.mainloop()
