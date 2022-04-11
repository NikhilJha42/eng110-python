class MoneyInput:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"You have deposited {self.value} "

    def __format__(self, format_spec):
        return f"You are about to deposit {self.value} in {format_spec}"

x = input("Please add deposit:")

new_deposit = MoneyInput(float(x))

print(f"{new_deposit:}")