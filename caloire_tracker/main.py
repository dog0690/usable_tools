import random
import time
class food():
    def __init__(self, name: str, protien: str, carbs: str, fats: str ) -> dict [str, int] :
        self.name = name
        self.protien = protien

class measurement():
    def __init__(self, macro: str, level: str, max_amount: int) -> dict [str, int]:
        self.macro = macro
        self.level = level
        self.max_amount = max_amount

    def High(self) -> int:
            high = (self.max_amount * random.uniform(20, 25))/100
            return f"{round(high, 2)}g"
        

protien = measurement('protine', 'H', 14)
carbs = measurement('carbs', 'H', 24)
fats = measurement('fats', 'H', 34)

def main():
    while True:
        print(measurement.High(protien))
        time.sleep(1)
main()