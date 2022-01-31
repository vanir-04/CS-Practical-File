# Program to find out words with three consecutive pairs of letters

user_input = str(input("Enter your sentence: "))

word_list = [(i.strip(',.')).lower() for i in user_input.split()]

c_count = 0
c_list = []

for word in word_list:
    for i in range(len(word)):
        if len(word) > 6 and i != len(word)-5 and word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
            c_list.append(word)
        elif len(word) > 6 and i == len(word)-5:
            break
        elif len(word) < 6:
            break
        else:
            continue

if len(c_list) == 0:
    print('There are no words with three consecutive pairs of letters in the sentence.')
elif len(c_list) == 1:
    print('The word with three consecutive letters is: '+str(c_list)[1:-1]+'.')
else:
    print('The words with three consecutive letters are: '+str(c_list)[1:-1]+'.')