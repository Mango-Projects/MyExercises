from random import choices
from string import hexdigits

def get_hex_verify_code(units:int=4, unit_length:int=4, symbol:str='-', **options):
    """generator a verify code

    Args:
        units (int, optional): count of units. Defaults to 4.
        unit_length (int, optional): length of unit. Defaults to 4.
        symbol (str, optional): Connection Symbol. Defaults to '-'.
    """
    return symbol.join(''.join(choices(hexdigits, k=unit_length)) for i in range(units))

if __name__ == '__main__':
    print(get_hex_verify_code())