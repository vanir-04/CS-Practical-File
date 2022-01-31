# Text File Menu-driven Program 1

while True:
    f = open('Files/abcd.txt', 'r')

    print('\n[1] Display last three characters of each line\n[2] Display text in uppercase\n[3] Display uppercase characters and their number\n[4] Display number of vowels\n[5] Quit')
    try:
        useropt = int(input('\nSelect [1], [2], [3], [4], or [5]: '))
    except:
        print('\nPlease enter a number.')
        continue
    if useropt == 1:
        for i in f.readlines():
            print(i[-4:-1])
    elif useropt == 2:
        print('\n'+(f.read()).upper())
    elif useropt == 3:
        unum = 0
        ulist = []
        for i in f.read():
            if i.isupper():
                unum += 1
                ulist.append(i)
            else:
                continue
        print('Uppercase characters are:',*ulist,'\nNumber of uppercase characters is',unum)
    elif useropt == 4:
        vnum = 0
        for i in f.read():
            if i in 'AEIOUaeiou':
                vnum += 1
            else:
                continue
        print('\nNumber of vowels is',vnum)
    elif useropt == 5:
        f.close()
        break
    else:
        print('\nPlease choose a number between 1 and 4')
        continue