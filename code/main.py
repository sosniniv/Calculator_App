import tkinter as tk
from tkinter import ttk, messagebox
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")  # Установка заголовка окна
        self.geometry("362x641")  # Установка размера окна
        self.resizable(False, False)  # Отключение изменения размера окна
        
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 18), padding=10, width=5)  # Конфигурация стиля кнопок
        
        self.create_widgets()  # Создание виджетов (элементов интерфейса)
        
        self.bind('<KeyPress>', self.on_key_press)  # Привязка события клавиатуры
        self.bind('<Return>', lambda event: self.on_button_click('='))  # Привязка события нажатия Enter
    
    def create_widgets(self):
        self.result_var = tk.StringVar()  # Переменная для хранения результата
        
        # Поле ввода и отображения результата
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")  # Растягиваем поле и добавляем отступы
        
        # Растягиваем строку с полем ввода
        self.grid_rowconfigure(0, weight=1)
        
        # Определение кнопок и их расположение
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('√', 5, 1), ('^', 5, 2), ('%', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('ln', 6, 3),
            ('log', 7, 0), ('e^x', 7, 1), ('1/x', 7, 2), ('n!', 7, 3)
        ]
        
        # Создание кнопок и их размещение на сетке с использованием ttk.Button
        for (text, row, col) in buttons:
            button = ttk.Button(self, text=text, style='TButton', command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")
    
    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set("")  # Очистка поля ввода
        elif char == '=':
            try:
                expression = self.result_var.get()  # Получение выражения из поля ввода
                result = str(eval(expression))  # Вычисление результата
                self.result_var.set(result)  # Установка результата в поле ввода
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")  # Показ ошибки в случае невалидного ввода
        elif char == '√':
            try:
                expression = self.result_var.get()
                result = str(math.sqrt(eval(expression)))  # Вычисление квадратного корня
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
        elif char == 'sin':
            try:
                expression = self.result_var.get()
                result = str(math.sin(math.radians(eval(expression))))  # Вычисление синуса
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
        elif char == 'cos':
            try:
                expression = self.result_var.get()
                result = str(math.cos(math.radians(eval(expression))))  # Вычисление косинуса
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
        elif char == 'tan':
            try:
                expression = self.result_var.get()
                result = str(math.tan(math.radians(eval(expression))))  # Вычисление тангенса
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
        elif char == 'ln':
            try:
                expression = self.result_var.get()
                result = str(math.log(eval(expression)))  # Вычисление натурального логарифма
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
        elif char == 'log':
            try:
                expression = self.result_var.get()
                result = str(math.log10(eval(expression)))  # Вычисление десятичного логарифма
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
        elif char == 'e^x':
            try:
                expression = self.result_var.get()
                result = str(math.exp(eval(expression)))  # Вычисление экспоненциальной функции
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
        elif char == '1/x':
            try:
                expression = self.result_var.get()
                result = str(1 / eval(expression))  # Вычисление обратной величины
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
        elif char == 'n!':
            try:
                expression = self.result_var.get()
                result = str(math.factorial(eval(expression)))  # Вычисление факториала
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
        else:
            current_text = self.result_var.get()  # Получение текущего текста из поля ввода
            new_text = current_text + str(char)  # Добавление нового символа к текущему тексту
            self.result_var.set(new_text)  # Установка нового текста в поле ввода
    
    def on_key_press(self, event):
        key = event.char
        if key.isdigit() or key in '+-*/.=^%':
            self.on_button_click(key)
        elif key == '\x08':  # ASCII код для клавиши Backspace
            current_text = self.result_var.get()
            if current_text:
                new_text = current_text[:-1]  # Удаление последнего символа
                self.result_var.set(new_text)

if __name__ == "__main__":
    app = Calculator()  # Создание экземпляра класса Calculator
    app.mainloop()  # Запуск главного цикла приложения
