# CSV Menu-driven Program 1

import csv

def adddata():
    sampledata = [
        ['PID','PNAME','COST','QUANTITY'],
        ['P1','BRUSH',50,200],
        ['P2','TOOTHPASTE',120,150],
        ['P3','COMB',40,300],
        ['P4','SHEETS',100,500],
        ['P5','PEN',10,250]
    ]
    with open('Files/PRODUCT.CSV', 'w', newline='') as f:
        (csv.writer(f)).writerows(sampledata)

def disrec():
    print('')
    with open('Files/PRODUCT.CSV', 'r') as f:
        csvread = csv.reader(f)
        next(csvread)
        for i in csvread:
            print(i)
    
def copyrec():
    newrec = []
    with open('Files/PRODUCT.CSV', 'r') as f1:
        csvread = csv.reader(f1)
        newrec.append(next(csvread))
        for i in csvread:
            if int(i[3]) > 150:
                newrec.append(i)
    with open('Files/PRO1.CSV', 'w', newline='') as f2:
        (csv.writer(f2)).writerows(newrec)

def totalcost():
    costsum = 0
    with open('Files/PRODUCT.CSV', 'r') as f:
        csvread = csv.reader(f)
        next(csvread)
        for i in csvread:
            costsum += (int(i[2])*int(i[3]))
    print('\nTotal cost of all products is:',costsum)

def maxcost():
    highestcost = 0
    with open('Files/PRODUCT.CSV', 'r') as f:
        csvread = csv.reader(f)
        next(csvread)
        for i in csvread:
            if int(i[2]) > highestcost:
                highestcost = int(i[2])
        f.seek(0)
        next(csvread)
        for i in csvread:
            if int(i[2]) == highestcost:
                print('\nProduct with highest cost is:\n\n',i)

while True:
    print('\n[1] Add Sample Data\n[2] Display records\n[3] Copy records whose quantity is more than 150 to "PRO1.CSV"\n[4] Display total cost of all products\n[5] Show record with highest cost\n[6] Quit')
    try:
        useropt = int(input("\nSelect [1], [2], [3], [4], [5], or [6]: "))
    except:
        print('\nPlease enter a number.')
        continue
    if useropt == 1:
        adddata()
    elif useropt == 2:
        disrec()
    elif useropt == 3:
        copyrec()
    elif useropt == 4:
        totalcost()
    elif useropt == 5:
        maxcost()
    elif useropt == 6:
        break
    else:
        print('\nPlease enter a value between 1 and 4')