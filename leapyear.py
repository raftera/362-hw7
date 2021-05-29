def leapyear(year):
    if (not(isinstance(year, int))):
        raise ValueError('Please enter an integer')
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
         return True
    return False
