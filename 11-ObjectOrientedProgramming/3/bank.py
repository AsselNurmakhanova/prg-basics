from bankcode import Bank
def main():
    mybank = Bank("12 3456 5555 9090 1111 0000 7722")
    mybank.display_balance()
    mybank.deposit(25.30)
    mybank.display_balance()
    mybank.withdraw(31.70)
    mybank.display_balance()
    mybank.withdraw(14)
    mybank.display_balance()
if __name__ == "__main__":
    main()