from decimal import Decimal

class ToDecimal:
    def __init__(self, float_n):
        self.float_n = float_n

    def decimal_func(self):
        return f'{Decimal(r.float_n)}'


r = ToDecimal(56.73)
print(r.decimal_func())
