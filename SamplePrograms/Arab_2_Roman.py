num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), 
           (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), 
           (4, 'IV'), (1, 'I')]


"""
The function returns the roman numeral for a given number

>>> num2roman(1)
I

>>> num2roman(10)
X

>>> num2roman(4)
IV

>>> num2roman(5)
V

>>> num2roman(9)
IX

>>> num2roman(40)
XL

>>> num2roman(50)
L

>>> num2roman(90)
XC

>>> num2roman(100)
C

>>> num2roman(400)
XD

>>> num2roman(500)
D

>>> num2roman(1000)
M

>>> num2roman(900)
CM

>>> num2roman(600)
DC

>>> num2roman(999)
CMXCIX

"""
def num2roman(num):
    roman = ''
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman = roman +  r
                num = num - i
    return roman

if __name__ == "__main__":

    import doctest
    doctest.testmod()
    print(num2roman(100))
    print(num2roman(1000))
    print(num2roman(10001))
    print(num2roman(999))