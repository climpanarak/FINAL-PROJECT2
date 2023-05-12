import tkinter as tk
from GUIs import ExpenseTrackerApp

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()