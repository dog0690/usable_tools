class food():
    def __init__(self, name: str, protien: str, carbs: str, fats: str ) -> dict [str, int] :
        self.name = name
        self.protien = protien

class measurement():
    def __init__(self, macro: str, level: str, amount: int) -> dict [str, int]:
        self.macro = macro
        self.level = level
        self.amount = amount

    def High(self) -> int:
        if self.level == 'H':
            high = self.amount * .2
            return round(high, 2)
        

protien = measurement('protine', 'H', 14)
carbs = measurement('protine', 'H', 24)
fats = measurement('protine', 'H', 34)

print(measurement.High(protien))