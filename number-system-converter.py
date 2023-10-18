import tkinter as tk
from tkinter import simpledialog

def binary_to_decimal(binary):
    return int(binary, 2)


def binary_to_octal(binary):
    #binary to decimal
    decimal = binary_to_decimal(binary)

    # decimal to octal
    octal = oct(decimal)

    
    return str(octal).replace("0o", "")


def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    return hex(decimal).replace("0x", "")


def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")


def hexadecimal_to_binary(hexadecimal):
    decimal = int(hexadecimal, 16)
    return decimal_to_binary(decimal)


def create_gui():
    root = tk.Tk()
    root.geometry("400x300")
    root.title("Binary Converter")

    label = tk.Label(root, text="Choose an option:")
    label.pack(pady=10)

    def handle_choice(choice):
        if choice == 1:
            binary = simpledialog.askstring("Binary to Decimal", "Enter a binary number")
            result = binary_to_decimal(binary)
            result_label.config(text=f"Decimal: {result}")
        elif choice == 2:
            binary = simpledialog.askstring("Binary to Octal", "Enter a binary number")
            result = binary_to_octal(binary)
            result_label.config(text=f"Octal: {result}")
        elif choice == 3:
            binary = simpledialog.askstring("Binary to Hexadecimal", "Enter a binary number")
            result = binary_to_hexadecimal(binary)
            result_label.config(text=f"Hexadecimal: {result}")
        elif choice == 4:
            decimal = simpledialog.askinteger("Decimal to Binary", "Enter a decimal number")
            result = decimal_to_binary(decimal)
            result_label.config(text=f"Binary: {result}")
        elif choice == 5:
            hexadecimal = simpledialog.askstring("Hexadecimal to Binary", "Enter a hexadecimal number")
            result = hexadecimal_to_binary(hexadecimal)
            result_label.config(text=f"Binary: {result}")

    button1 = tk.Button(root, text="Binary to Decimal", command=lambda: handle_choice(1))
    button1.pack(pady=5)

    button2 = tk.Button(root, text="Binary to Octal", command=lambda: handle_choice(2))
    button2.pack(pady=5)

    button3 = tk.Button(root, text="Binary to Hexadecimal", command=lambda: handle_choice(3))
    button3.pack(pady=5)

    button4 = tk.Button(root, text="Decimal to Binary", command=lambda: handle_choice(4))
    button4.pack(pady=5)

    button5 = tk.Button(root, text="Hexadecimal to Binary", command=lambda: handle_choice(5))
    button5.pack(pady=5)

    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
