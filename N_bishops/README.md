# ♟️ N Bishops on N×N Chessboard

This is a simple Python program to place **N bishops** on an **N×N chessboard** such that **no two bishops attack each other diagonally**.  
The board is printed using `1` for bishops and `0` for empty cells.

---

## 📌 Problem Statement

Place exactly `N` bishops on an `N×N` board so that:

- No two bishops attack each other diagonally.
- Print **one valid** board configuration using `1` and `0`.

Example for `N = 4`:
1 0 0 0
0 0 1 0
1 0 0 0
0 0 0 1

---

## 🛠️ How It Works

- The board is created using a 2D list.
- The program checks diagonals using:
  - `main_diagonal = row - col`
  - `anti_diagonal = row + col`
- It places bishops only if the diagonals are not already used.

---

## 🚀 How to Run the Program

1. Make sure Python is installed on your computer.
2. Clone the repository or copy the code.
3. Run the script:

```bash
python bishops.py
```
Input any value of N (like 3, 4, 5, etc.).
👨‍🎓 Suitable For
First-year CSE students

Python beginners

Anyone learning basic problem solving with 2D lists and logic

📄 License
This project is open-source and free to use for learning.

---

Let me know if you want me to include a `.gitignore` file or add comments to the actual code in the repo!
