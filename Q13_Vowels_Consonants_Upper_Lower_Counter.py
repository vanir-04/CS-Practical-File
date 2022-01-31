# Program to read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file

f = open('Files/text.txt', 'r')

volist = []
colist = []
uplist = []
lolist = []

for i in f.read():
    if i in 'aeiouAEIOU':
        volist.append(i)
        if i.isupper():
            uplist.append(i)
        else:
            lolist.append(i)
    elif i not in 'aeiouAEIOU':
        colist.append(i)
        if i.isupper():
            uplist.append(i)
        else:
            lolist.append(i)
    else:
        continue

f.seek(0)
print(f.read())
print('\nNumber of vowels is',len(volist),
        '\nNumber of consonants is',len(colist),
        '\nNumber of uppercase characters is',len(uplist),
        '\nNumber of lowercase characters is',len(lolist))
f.close()