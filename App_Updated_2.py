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

        Label(window, text="Start Date (MM/DD/YYYY)").grid(row=4, column=1, padx=10, pady=10, sticky=W)
        self.startDateVar = StringVar()
        Entry(window, textvariable=self.startDateVar, justify=RIGHT).grid(row=4, column=2, padx=10, pady=10)

        Label(window, text="Extra Payment ($)").grid(row=5, column=1, padx=10, pady=10, sticky=W)
        self.extraPaymentVar = StringVar()
        Entry(window, textvariable=self.extraPaymentVar, justify=RIGHT).grid(row=5, column=2, padx=10, pady=10)

        # Create output fields
        Label(window, text="Monthly Payment ($)").grid(row=6, column=1, padx=10, pady=10, sticky=W)
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable=self.monthlyPaymentVar).grid(row=6, column=2, padx=10, pady=10, sticky=E)

        Label(window, text="Total Payment ($)").grid(row=7, column=1, padx=10, pady=10, sticky=W)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable=self.totalPaymentVar).grid(row=7, column=2, padx=10, pady=10, sticky=E)

        # Create buttons
        btComputePayment = Button(window, text="Compute Payment", command=self.computePayment).grid(row=8, column=2, padx=10, pady=10, sticky=E)

        btClear = Button(window, text="Clear", command=self.clearFields).grid(row=8, column=1, padx=10, pady=10, sticky=W)

        # Create table
        columns = ("Payment Date", "Payment Amount ($)", "Principal ($)", "Interest ($)", "Balance ($)")
        self.tree = ttk.Treeview(window, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.grid(row=9, column=1, columnspan=2, padx=10, pady=10)

        window.mainloop()

    def computePayment(self):
        try:
            loanAmount = float(self.loanAmountVar.get())
            annualInterestRate = float(self.annualInterestRateVar.get())
            numberOfYears = int(self.numberOfYearsVar.get())
            startDate = self.startDateVar.get()
            extraPayment = float(self.extraPaymentVar.get())

            monthlyPayment, totalPayment, tableData = self.calculateAmortization(loanAmount, annualInterestRate, numberOfYears, startDate, extraPayment)

            self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
            self.totalPaymentVar.set(format(totalPayment, '10.2f'))

            self.populateTable(tableData)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid input values.")

    def clearFields(self):
        self.loanAmountVar.set("")
        self.annualInterestRateVar.set("")
        self.numberOfYearsVar.set("")
        self.startDateVar.set("")
        self.extraPaymentVar.set("")
        self.monthlyPaymentVar.set("")
        self.totalPaymentVar.set("")
        self.tree.delete(*self.tree.get_children())


        def calculateAmortization(self, loanAmount, annualInterestRate, numberOfYears, startDate, extraPayment):
            monthlyInterestRate = annualInterestRate / 1200
            numberOfPayments = numberOfYears * 12
            monthlyPayment = self.getMonthlyPayment(loanAmount, monthlyInterestRate, numberOfPayments)
            totalPayment = monthlyPayment * numberOfPayments
            balance = loanAmount
            tableData = []

            for i in range(numberOfPayments):
                interest = balance * monthlyInterestRate
                principal = monthlyPayment - interest
                balance = balance - principal - extraPayment

                if balance < 0:
                    balance = 0

                paymentDate = self.getPaymentDate(startDate, i)
                tableData.append((paymentDate, monthlyPayment, principal, interest, balance))

            return monthlyPayment, totalPayment, tableData
