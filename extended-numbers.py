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
        self.__exnumber = None
        self.__update_exnumber()

    def __add__(self, other : int): 
        if self.__instanceable:
            return ExtendedNumber(self.__number + other, precision = self.__precision, instanceable = self.__instanceable) 
        self.__number += other
        self.__update_exnumber()
        return self
    
    __radd__ = __add__

    def __str__(self : int) -> str: 
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

    def __update_exnumber(self) -> None:
        self.__exnumber = self.convert(str(self.__number), self.__precision)

    def custom_conversions(self, custom_conversions : dict) -> None:
        self.__class__.CONVERSIONS = custom_conversions
        self.__update_exnumber()

# Example use : number = ExtendedNumber(450, precision = 3, instanceable = True)
