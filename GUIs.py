import tkinter as tk
import csv
from datetime import date

class ExpenseTrackerApp:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Expense Tracker")
        self.master.resizable(False, False)

        self.label_expense = tk.Label(self.master, text="Enter expense:")
        self.label_expense.grid(row=0, column=0)

        self.entry_expense = tk.Entry(self.master)
        self.entry_expense.grid(row=0, column=1)

        self.label_amount = tk.Label(self.master, text="Enter amount:")
        self.label_amount.grid(row=1, column=0)

        self.entry_amount = tk.Entry(self.master)
        self.entry_amount.grid(row=1, column=1)

        self.button_add = tk.Button(self.master, text="Add Expense", command=self.add_expense)
        self.button_add.grid(row=2, column=0)

        self.button_clear = tk.Button(self.master, text="Clear Fields", command=self.clear_fields)
        self.button_clear.grid(row=2, column=1)

        self.button_clear_list = tk.Button(self.master, text="Clear List", command=self.clear_list)
        self.button_clear_list.grid(row=2, column=2)

        self.listbox_expenses = tk.Listbox(self.master)
        self.listbox_expenses.grid(row=3, column=0, columnspan=3)

        self.label_total = tk.Label(self.master, text="Total Expenses: $0.00")
        self.label_total.grid(row=4, column=0, columnspan=3)

        self.expenses = []
        self.total_expenses = 0.0

    def add_expense(self):
        expense = self.entry_expense.get()
        amount_str = self.entry_amount.get()


        if not expense:
            self.label_total.config(text="Please enter an expense.", fg="red")
            return
        elif not amount_str:
            self.label_total.config(text="Please enter an amount.", fg="red")
            return

        try:
            amount = float(amount_str)
        except ValueError:
            self.label_total.config(text="Amount must be a number.", fg="red")
            return

        self.expenses.append((expense, amount))
        self.total_expenses += amount

        self.listbox_expenses.insert(tk.END, f"{expense}: ${amount:.2f}")
        self.label_total.config(text=f"Total Expenses: ${self.total_expenses:.2f}", fg="black")

        self.clear_fields()
        self.save_expenses_to_csv()

    def clear_fields(self):
        self.entry_expense.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)

    def clear_list(self):
        self.expenses = []
        self.total_expenses = 0.0
        self.listbox_expenses.delete(0, tk.END)
        self.label_total.config(text="Total Expenses: $0.00", fg="black")

        self.save_expenses_to_csv()

    def save_expenses_to_csv(self):
        filename = f"expenses_{date.today()}.csv"

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Expense', 'Amount'])

            for expense, amount in self.expenses:
                writer.writerow([expense, amount])

