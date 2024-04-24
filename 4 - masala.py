# 4 - masala

from collections import namedtuple
Car = namedtuple('Car', ['model', 'color', 'year'])


class Cars(Car):
    def __new__(cls, model, color, year, price):
        return super().__new__(cls, model, color, year)



    def __init__(self, model, color, year, price):
        self.price = price

    def output(self):
        return f'Model: {a.model}\nColor: {a.color}\nYear: {a.year}\nPrice: {a.price}'


a = Cars('BMWX8', 'Blue', '2021', '$220.000')
print(a.output())