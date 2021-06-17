
class ExtendedNumber(): 

    CONVERSIONS = {"k" : 3, "M" : 6, "B" : 9, "T" : 12}

    def __init__(self, number, **kwargs): 
        self.__number = number
        self.precision = kwargs.get("precision", 1)
        self.exnumber = None

        self.update_exnumber()

    def __add__(self, other): 
        if isinstance(other, ExtendedNumber):
            return ExtendedNumber(self.number + other.number, precision = self.precision)
        return ExtendedNumber(self.number + other, precision = self.precision)

    def __sub__(self, other): 
        if isinstance(other, ExtendedNumber): 
            return ExtendedNumber(self.number - other, percision = self.precision)
        return ExtendedNumber(self.number - other.number, precision = self.precision)
        
    __radd__ = __add__
    __rsub__ = __sub__

    def __repr__(self): 
        return self.exnumber

    @property
    def number(self): 
        return self.__number

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
            to_return = str(round(0.001 * int(number), 4)) + list(__class__.CONVERSIONS.keys())[0]
            to_return = to_return if not negative else "-" + to_return
            return to_return

    def update_exnumber(self) -> None:
        self.exnumber = self.convert(str(self.number), self.precision)

    def custom_conversions(self, custom_conversions : dict) -> None:
        self.__class__.CONVERSIONS = custom_conversions
        self.update_exnumber()

# Example use : number = ExtendedNumber(450, precision = 3)
