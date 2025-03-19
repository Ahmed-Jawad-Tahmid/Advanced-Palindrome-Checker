import tkinter as tk
from tkinter import messagebox
import socket
import time  

# Server configuration
SERVER_HOST = 'localhost'
SERVER_PORT = 12345
MAX_RETRIES = 3  # Retry up to 3 times if the server does not respond
TIMEOUT_DURATION = 5  # 5-second timeout per attempt

def send_request():
    """ Sends the user's input to the server and displays the result. """
    user_input = entry.get().strip()
    if not user_input:
        messagebox.showerror("Error", "Please enter a string to check.")
        return

    check_type = "simple" if check_var.get() == 1 else "complex"
    message = f"{check_type}|{user_input}"
    
    retries = 0

    while retries < MAX_RETRIES:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.settimeout(TIMEOUT_DURATION)  # Set timeout for response
                client_socket.connect((SERVER_HOST, SERVER_PORT))
                client_socket.send(message.encode())

                # Attempt to receive response within the timeout duration
                response = client_socket.recv(1024).decode()
                response_label.config(text=f"Server Response:\n{response}", fg="green")
                return  # Exit function if successful

        except socket.timeout:
            retries += 1
            messagebox.showwarning("Timeout", f"Server did not respond. Retrying ({retries}/{MAX_RETRIES})...")
            time.sleep(2)  # Wait before retrying

        except ConnectionRefusedError:
            messagebox.showerror("Error", "Unable to connect to the server. Please try again later.")
            return

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            return

    # If maximum retries are exceeded
    messagebox.showerror("Error", "Server is unreachable after multiple attempts. Please try again later.")

# Create the main GUI window
root = tk.Tk()
root.title("Advanced Palindrome Checker")
root.geometry("650x500")  # Increased window size
root.configure(bg="#f0f5f9")

# Title Label
title_label = tk.Label(root, text="Palindrome Checker", font=("Arial", 22, "bold"), fg="#004466", bg="#f0f5f9")
title_label.pack(pady=20)

# Entry Field for user input
entry_frame = tk.Frame(root, bg="#f0f5f9")
entry_frame.pack(pady=10)
entry = tk.Entry(entry_frame, width=35, font=("Arial", 16), bd=3, relief="solid")
entry.pack(ipady=8)

# Radio Buttons for Simple/Complex Check
check_var = tk.IntVar(value=1)
radio_frame = tk.Frame(root, bg="#f0f5f9")
radio_frame.pack(pady=15)

tk.Radiobutton(radio_frame, text="Simple Palindrome Check", variable=check_var, value=1,
               font=("Arial", 16, "bold"), bg="#f0f5f9", activebackground="#cce7ff").pack(anchor="w", padx=20)
tk.Radiobutton(radio_frame, text="Complex Palindrome Check", variable=check_var, value=2,
               font=("Arial", 16, "bold"), bg="#f0f5f9", activebackground="#cce7ff").pack(anchor="w", padx=20)

# Check Button
check_button = tk.Button(root, text="Check", font=("Arial", 16, "bold"), fg="white", bg="#0088cc",
                         activebackground="#006699", activeforeground="white",
                         command=send_request, relief="raised", bd=5,
                         padx=40, pady=15)
check_button.pack(pady=25)

# Label to Display Response
response_label = tk.Label(root, text="", font=("Arial", 14), fg="#004466", bg="#f0f5f9", wraplength=550, justify="center")
response_label.pack(pady=15)

# Run the GUI event loop
root.mainloop()
