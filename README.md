# Getting Started with Palindrome Checker

This project is a **TCP-based Client-Server Palindrome Checker** with a Tkinter GUI, supporting both **basic** and **advanced** palindrome analysis.

---

## How to Use

In the project directory, you can run:

### `python Server.py`
Starts the **server** and begins listening for client connections.

- The server logs all incoming requests.
- It processes both **simple** and **complex** palindrome checks.
- The console displays connection details.

<br>

### `python Client.py`
Launches the **GUI client** for user input.

- Users can enter a string and select a **check mode**.
- The request is sent to the **server** for processing.
- The result is displayed in the GUI window.

---

## Example Usage

### 📌 Simple Check  
<img src="https://github.com/Ahmed-Jawad-Tahmid/Advanced-Palindrome-Checker/blob/main/Simple_palindrome_check.png?raw=true" alt="Simple Check Screenshot" width="500" height="400">

<br>

### 📌 Complex Check  
<img src="https://github.com/Ahmed-Jawad-Tahmid/Advanced-Palindrome-Checker/blob/main/Complex_palindrome_check.png?raw=true" alt="Complex Check Screenshot" width="500" height="400">

<br>

<img src="https://github.com/Ahmed-Jawad-Tahmid/Advanced-Palindrome-Checker/blob/main/Complex_palindrom_check2.jpg?raw=true" alt="Complex Palindrome Check Score" width="500" height="400">

---

## Understanding the Complexity Score

The **Complexity Score** represents the **minimum number of swaps** required to transform the given string into a palindrome.

- **If the score is `0`**, the string is already a palindrome.
- **A higher score** means more swaps are needed to rearrange the characters into a palindrome.
- **If "Can form a palindrome" is `False`**, the string cannot be rearranged into a palindrome, and no swaps are possible.
