# Integer to Roman

# Declare fundamental roman numbers
int_list = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
roman_list = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')

# Take input from user
inp_num = int(input("Please enter the number that you want to convert to Roman Numerals: "))

romantext = ''

# Conversion to Roman
for i in range(len(int_list)):
    quot = int((inp_num)/(int_list[i]))
    romantext += str((roman_list[i])*(quot))
    inp_num -= (int_list[i])*(quot)

print(romantext)