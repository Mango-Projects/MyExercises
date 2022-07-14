from random import choices
from string import hexdigits, ascii_letters

def get_verify_code(unit_text: str="hex" ,units:int=4, unit_length:int=4, symbol:str='-') -> str:
    """generator a verify code

    Args:
        units (int, optional): count of units. Defaults to 4.
        unit_length (int, optional): length of unit. Defaults to 4.
        symbol (str, optional): Connection Symbol. Defaults to '-'.
    """
    match unit_text:
        case "hex" | "HEX" | "Hexadecimal":
            text = hexdigits
        case "ascii" | "ASCII":
            text = ascii_letters
        case "int" | "INT" | "num" | "Num" | "number" | "Number":
            text = "".join(map(str, range(10)))
        case _:
            text = unit_text

    def bit_gen(): return ''.join(choices(text, k=unit_length))
    return symbol.join(bit_gen() for i in range(units))



if __name__ == '__main__':
    print(get_verify_code())