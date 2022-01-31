# CSV Menu-driven Program 2

import csv

def adddata():
    sampledata = [
        ['TID','DESTINATION','DAYS','FARE'],
        ['T10','AUSTRALIA',10,300],
        ['T11','AUSTRIA',15,750],
        ['T12','RAJASTHAN',10,700],
        ['T13','FRANCE',12,650]
    ]
    with open('Files/Tour.csv', 'w', newline='') as f:
        (csv.writer(f)).writerows(sampledata)

def disrec():
    print('')
    with open('Files/Tour.csv', 'r') as f:
        csvread = csv.reader(f)
        next(csvread)
        for i in csvread:
            print(i)

def findrec():
    print('')
    found = False
    with open('Files/Tour.csv', 'r') as f:
        csvread = csv.reader(f)
        next(csvread)
        for i in csvread:
            if int(i[3]) > 500 and int(i[3]) < 750:
                print(i)
                found = True
    if found is False:
        print('\nNo such record found.')

while True:
    print('\n[1] Add Sample Data\n[2] Display records\n[3] Display records where fare is between 500 and 750\n[4] Quit')
    try:
        useropt = int(input("\nSelect [1], [2], [3], or [4]: "))
    except:
        print('\nPlease enter a number.')
        continue
    if useropt == 1:
        adddata()
    elif useropt == 2:
        disrec()
    elif useropt == 3:
        findrec()
    elif useropt == 4:
        break
    else:
        print('\nPlease enter a value between 1 and 4')