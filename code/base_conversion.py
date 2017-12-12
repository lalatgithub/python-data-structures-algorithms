def convert_to_string(number, base):
    
    allowed_str = '012345679ABCDEF' # includes Binary, Octal, Decimal and Hex
    
    if number < base: # can be number % base == number or can be number // base == 0
        return allowed_str[number]
    
    return convert_to_string(number // base, base) + allowed_str[number % base]
  
num = 23
base = 2

print(type(num))

result = convert_to_string(num, base)
print(result, type(result))
