# Text File Menu-driven Program 2

while True:
    f1 = open('Files/abcd.txt', 'r+')

    print('\n[1] Copy content to Copy.txt\n[2] Find frequency of a word\n[3] Copy lines starting with "the" to copy2.txt\n[4] Replace "This" with "That"\n[5] Remove "This" and display file\n[6] Quit')
    try:
        useropt = int(input("\nSelect [1], [2], [3], [4], [5], or [6]: "))
    except:
        print('\nPlease enter a number.')
        continue
    if useropt == 1:
        with open('Files/Copy.txt', 'w+') as f2:
            f2.write(f1.read())
            f2.seek(0)
            print("\nText in",f2.name+':\n\n'+f2.read())
        continue
    elif useropt == 2:
        wordopt = input('\nPlease type the word you want to find the frequency of: ')
        freq = 0
        for i in (f1.read()).split():
            if wordopt == i.strip(',.\n'):
                freq += 1
            else:
                continue
        print('\nThe word appears',freq,'times.')
        continue
    elif useropt == 3:
        thelist = []
        for i in f1.readlines():
            if (i.split())[0] == 'the':
                thelist.append(i)
            else:
                continue
        with open('Files/copy2.txt', 'w+') as f3:
            f3.writelines(thelist)
            f3.seek(0)
            print('\nText in',f3.name+':\n\n'+f3.read())
        continue
    elif useropt == 4:
        newcon = (f1.read()).replace('This','That')
        f1.seek(0)
        f1.truncate()
        f1.write(newcon)
        f1.seek(0)
        print('Text after replacing:\n\n'+f1.read())
        continue
    elif useropt == 5:
        print('\n'+(f1.read()).replace('This',''))
        continue
    elif useropt == 6:
        f1.close()
        break
    else:
        print('\nPlease choose a number between 1 and 6')
        continue