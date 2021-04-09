def inte(value):
    if int(value) <= 9:
        value = '0' + str(value)
    else:
        value = str(value)
    return value
