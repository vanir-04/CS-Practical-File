# Binary File Menu-driven Program 2

import pickle

def entrec(admno,name,perc):
    record = [admno,name,perc]
    with open('Files/STUQ2.DAT','ab') as f:
        pickle.dump(record,f)

def disrec():
    print('')
    with open('Files/STUQ2.DAT', 'rb') as f:
        while True:
            try:
                print(pickle.load(f))
            except EOFError:
                break

def condrec():
    print('')
    with open('Files/STUQ2.DAT', 'rb') as f:
        while True:
            try:
                currec = pickle.load(f)
                if (currec)[2] > 75:
                    print(currec)
            except EOFError:
                break

while True:
    print('\n[1] Enter records\n[2] Display records\n[3] Display records with percentage above 75\n[4] Quit')
    try:
        useropt = int(input("\nSelect [1], [2], [3], or [4]: "))
    except:
        print('\nPlease enter a number.')
        continue
    if useropt == 1:
        try:
            entrec(input('\nEnter Admission Number: '),
            input('Enter Name of Student: '),
            float(input('Enter Marks Percentage of Student: ')))
        except:
            print('\nPlease enter a float value for percentage.')
    elif useropt == 2:
        disrec()
    elif useropt == 3:
        condrec()
    elif useropt == 4:
        break
    else:
        print('\nPlease enter a value between 1 and 4')