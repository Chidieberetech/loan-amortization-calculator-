from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.geometry("500x400")

        # Create input fields
        Label(window, text="Loan Amount ($)").grid(row=1, column=1, padx=10, pady=10, sticky=W)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=1, column=2, padx=10, pady=10)

        Label(window, text="Annual Interest Rate (%)").grid(row=2, column=1, padx=10, pady=10, sticky=W)
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=2, column=2, padx=10, pady=10)

        Label(window, text="Loan Term (Years)").grid(row=3, column=1, padx=10, pady=10, sticky=W)
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=3, column=2, padx=10, pady=10)

        # Create a button to calculate the loan
        Button(window, text="Calculate", command=self.calculate).grid(row=4, column=2, padx=10, pady=10)

        window.mainloop()

    def calculate(self):
        # Implement your calculation logic here
        pass

LoanCalculator()