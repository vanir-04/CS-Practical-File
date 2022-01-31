# Maximum and Minimum values from a list of 5 integers

# Inputting Numbers
num_list = []
i = 0
while i < 5:
    try:
        num_inp = int(input(str(i+1)+". Enter an integer: "))
        num_list.append(num_inp)
        i += 1
    except:
        print('Please enter an integer.\n')
        continue

# Finding the Max and Min values from the list
max_num = max(num_list)
min_num = min(num_list)

# Result
print("\nThe greatest number is", str(max_num), "and the smallest number is", str(min_num)+'.')