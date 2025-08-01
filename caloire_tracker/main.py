import random
import time
class my_macro():
    def __init__(self, name: str, protien: int, carbs: int, fats: int ) -> dict [str, int] :
        self.name = name
        self.protien = protien
        self.carbs = carbs
        self.fats = fats

class food():
    def __init__(self, macro: str, level: str, max_amount: int) -> dict [str, int]:
        self.macro = macro
        self.level = level
        self.max_amount = max_amount

#    def High(self) -> int:
#            high = (self.max_amount * random.uniform(20, 25))/100
#            return f"{round(high, 2)}g"
    def count(self, level) -> int:
            if level == "H":
                high = (self.max_amount * random.uniform(20, 25))/100
                amount = f"{round(high, 2)}g"
            elif level == "M":
                medium = (self.max_amount * random.uniform(14, 19))/100
                amount=  f"{round(medium, 2)}g"
            elif level == "L":
                low = (self.max_amount * random.uniform(9, 13))/100
                amount=  f"{round(low, 2)}g"
            else:
                amount = "please enter H, M, L"
            return amount

me = my_macro('charley',124, 250, 34 )
cookie = food('protien', 'H', me.protien)
def main():
    while True:
        print(food.count(cookie, cookie.level))
        time.sleep(1)
main()