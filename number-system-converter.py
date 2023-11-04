import tkinter as tk
from tkinter import simpledialog, messagebox

def binary_to_decimal(binary):
    try:
        return int(binary, 2)
    except ValueError:
        messagebox.showerror("Error", "Invalid binary number")
        return None

def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    if decimal is not None:
        return oct(decimal).replace("0o", "")

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    if decimal is not None:
        return hex(decimal).replace("0x", "")

def decimal_to_binary(decimal):
    try:
        return bin(decimal).replace("0b", "")
    except ValueError:
        messagebox.showerror("Error", "Invalid decimal number")
        return None

def hexadecimal_to_binary(hexadecimal):
    try:
        decimal = int(hexadecimal, 16)
        return decimal_to_binary(decimal)
    except ValueError:
        messagebox.showerror("Error", "Invalid hexadecimal number")
        return None

def create_gui():
    root = tk.Tk()
    root.geometry("400x300")
    root.title("Binary Converter")

    label = tk.Label(root, text="Choose an option:")
    label.pack(pady=10)

    def handle_choice(choice):
        if choice == 1:
            binary = simpledialog.askstring("Binary to Decimal", "Enter a binary number")
            if binary is not None:
                result = binary_to_decimal(binary)
                if result is not None:
                    result_label.config(text=f"Decimal: {result}")
        elif choice == 2:
            binary = simpledialog.askstring("Binary to Octal", "Enter a binary number")
            if binary is not None:
                result = binary_to_octal(binary)
                if result is not None:
                    result_label.config(text=f"Octal: {result}")
        elif choice == 3:
            binary = simpledialog.askstring("Binary to Hexadecimal", "Enter a binary number")
            if binary is not None:
                result = binary_to_hexadecimal(binary)
                if result is not None:
                    result_label.config(text=f"Hexadecimal: {result}")
        elif choice == 4:
            decimal = simpledialog.askinteger("Decimal to Binary", "Enter a decimal number")
            if decimal is not None:
                result = decimal_to_binary(decimal)
                if result is not None:
                    result_label.config(text=f"Binary: {result}")
        elif choice == 5:
            hexadecimal = simpledialog.askstring("Hexadecimal to Binary", "Enter a hexadecimal number")
            if hexadecimal is not None:
                result = hexadecimal_to_binary(hexadecimal)
                if result is not None:
                    result_label.config(text=f"Binary: {result}")

    options = ["Binary to Decimal", "Binary to Octal", "Binary to Hexadecimal", "Decimal to Binary", "Hexadecimal to Binary"]

    for index, option in enumerate(options, start=1):
        button = tk.Button(root, text=option, command=lambda i=index: handle_choice(i))
        button.pack(pady=5)

    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
