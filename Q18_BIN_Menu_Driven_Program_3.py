# Binary File Menu-driven Program 3

import pickle

def entrec(vtype,wheelno):
    vrec = (vtype,wheelno)
    with open('Files/vehicle.dat', 'ab') as f:
        pickle.dump(vrec,f)

def disrec():
    print('')
    with open('Files/vehicle.dat', 'rb') as f:
        while True:
            try:
                print(pickle.load(f))
            except EOFError:
                break
    
def countrec():
    reccount = 0
    with open('Files/vehicle.dat', 'rb') as f:
        try:
            for i in pickle.load(f):
                reccount += 1
        except:
            pass
    print('\nNumber of records is:',reccount)

while True:
    print('\n[1] Enter records\n[2] Display records\n[3] Display number of records\n[4] Quit')
    try:
        useropt = int(input("\nSelect [1], [2], [3], or [4]: "))
    except:
        print('\nPlease enter a number.')
        continue
    if useropt == 1:
        try:
            entrec(input('\nEnter Vehicle Type: '),
            int(input('Enter Number of Wheels: ')))
        except:
            print('\nPlease enter an integer value for number of wheels.')
    elif useropt == 2:
        disrec()
    elif useropt == 3:
        countrec()
    elif useropt == 4:
        break
    else:
        print('\nPlease enter a value between 1 and 4')