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
            if level == "h":
                high = (self.max_amount * random.uniform(20, 25))/100
                amount = f"{round(high, 2)}g"
            elif level == "m":
                medium = (self.max_amount * random.uniform(14, 19))/100
                amount=  f"{round(medium, 2)}g"
            elif level == "l":
                low = (self.max_amount * random.uniform(9, 13))/100
                amount=  f"{round(low, 2)}g"
            else:
                amount = "please enter H, M, L"
            return amount

me = my_macro('charley',124, 250, 34 )
cookie = food('protien', 'H', me.protien)
def main():
    print('Enter Your protien')
    fodo_name =  'cookie ' #input("name of your food? : ")
    protien = "m" #input("protien levle? : ")
    carbs = "h" #input("carbs level? : ")
    fats= "m" #input("fats level? : ")

    for i in range(3):
        macros =['protien', 'carbs', 'fats']
        macros_amt = [protien, carbs, fats]
        me_macros = [me.protien, me.carbs, me.fats]
        food_obj = food(macros[i], macros_amt[i], me_macros[i])
        macro_amount = food_obj.count(macros_amt[i])
        print(f"{macros[i]:10} {macro_amount}")

main()