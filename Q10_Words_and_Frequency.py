# Program to find the frequency of words appearing in a string
words = str(input("Enter a string: "))
words_list = words.split()
word_freq_dict = {}

for i in words_list:
    if i in word_freq_dict:
        word_freq_dict[i] += 1
    else:
        word_freq_dict[i] = 1

print(word_freq_dict)

final_dict = {}

for key, value in word_freq_dict.items():
    if value not in final_dict:
        final_dict[value] = [key]
    else:
        final_dict[value].append(key)
    
print(final_dict)