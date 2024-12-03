import tkinter
import customtkinter
import random

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

letters = 'qwertyuiopasdfghjklzxcvbnm'
symbols = '_/,.;!@#$%^&*()_+=-'
numbers = '0123456789'
chars = list(numbers+letters+letters.upper()+symbols)

# Функция проверки сложности пароля и определения его уровня надежности
def check_password_strength(password):
    # Определяем количество уникальных символов в пароле
    unique_chars = len(set(password))
    # Определяем длину пароля
    length = len(password)
    # Определяем сложность пароля
    if length < 8 or unique_chars < 5:
        return "Слабый"
    elif length < 12 or unique_chars < 8:
        return "Средний"
    else:
        return "Сильный"

# Алгоритм Генерации
def generate():
    len_password = int(entry_len.get())
    count_passwords = int(entry_count.get())
    for i in range(count_passwords):
        password = ''
        for j in range(len_password):
            password+=random.choice(chars)
        # Получаем уровень надежности пароля
        strength = check_password_strength(password)
        Input_filed.insert(tkinter.END, f"Пароль: {password} - Уровень надежности: {strength}\n")

def save_passwords():
    passwords = Input_filed.get("1.0", tkinter.END)  # Получаем все пароли из текстового поля
    with open("saved_passwords.txt", "w") as file:
        file.write(passwords)  # Записываем пароли в файл
    customtkinter.messagebox.showinfo("Сохранение", "Пароли успешно сохранены в файл saved_passwords.txt")  # Выводим сообщение об успешном сохранении



# Функция очистки
def clear():
    Input_filed.delete(0.0, tkinter.END)

window = customtkinter.CTk()
window.title('Генератор паролей')
window.geometry('600x600')

customtkinter.CTkLabel(window, text='Кол-во паролей:').place(x=180, y=30)
entry_count = customtkinter.CTkEntry(window, width=50)
entry_count.place(x=290, y=30)

customtkinter.CTkLabel(window, text='Длина паролей:').place(x=180, y=60)
entry_len = customtkinter.CTkEntry(window, width=50)
entry_len.place(x=290, y=58)

key_clear = customtkinter.CTkButton(window, text='Очистить', command=clear)
key_clear.place(x=430, y=100)

key_generate = customtkinter.CTkButton(window, text='Сгенерировать', command=generate)
key_generate.place(x=25, y=100)

Input_filed = customtkinter.CTkTextbox(window, width=560, height=380)
Input_filed.place(x=20, y=130)

key_save = customtkinter.CTkButton(window, text='Сохранить пароли', command=save_passwords)
key_save.place(x=230, y=100)

window.mainloop()