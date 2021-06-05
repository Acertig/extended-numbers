class AutoAttributeSetter:
    def __setattr__(self, attr, value): 
        if not (getattr(self, attr, value) and callable(value) and attr.startswith("__")): 
            super().__setattr__(attr, value)

class ExtendedNumber(AutoAttributeSetter): 

    CONVERSIONS = {"k" : 3, "M" : 6, "B" : 9, "T" : 12}

    def __init__(self, number, **kwargs): 
        self.__number = number
        self.__precision = kwargs.get("precision", 1)
        self.__instanceable = kwargs.get("instanceable", False)
        self.__exnumber = __class__.convert(str(self.__number), self.__precision)

    def __str__(self) -> str: 
        return self.__exnumber

    @staticmethod
    def convert(number : str, precision : int) -> str:
        props = None
        negative = False if number[0] != "-" else True
        number = number if number[0] != "-" else f"{number[1::]}"
        for conversion, digit in __class__.CONVERSIONS.items(): 
            lenght = len(number) 
            if lenght > digit: 
                props = (lenght, digit, conversion) 
        if props: 
            diff = props[0] - props[1] 
            before, after = (number[0:diff], number[diff:diff + precision])
            return before + "." + after + props[2]
        else: 
            to_return = str(round(0.001 * int(number), 4)) + "k"
            to_return = to_return if not negative else "-" + to_return
            return to_return
       
# Example use : number = ExtendedNumber(450, precision = 3, instanceable = True)
