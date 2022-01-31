# Binary File Menu-driven Program 1

import pickle

def entrec(pcode,pdesc,stock):
    record = {'prod_code':pcode, 'prod_desc':pdesc, 'stock':stock}
    with open('Files/PRODUCT.DAT', 'ab') as f:
        pickle.dump(record,f)

def disrec():
    print('')
    with open('Files/PRODUCT.DAT', 'rb') as f:
        while True:
            try:
                print(pickle.load(f))
            except EOFError:
                break
            

def updstock(pcode):
    datalist = []
    with open('Files/PRODUCT.DAT', 'rb+') as f:
        while True:
            try:
                rec = pickle.load(f)
                datalist.append(rec)
            except EOFError:
                break
        for i in datalist:
            if i['prod_code'] == pcode:
                try:
                    i['stock'] = int(input('Enter new value of stock: '))
                    break
                except:
                    print('\nPlease enter an integer value for stock.')
                    break
            else:
                continue
        f.seek(0)
        for i in datalist:
            pickle.dump(i,f)

while True:
    print('\n[1] Enter records\n[2] Display records\n[3] Update records\n[4] Quit')
    try:
        useropt = int(input("\nSelect [1], [2], [3], or [4]: "))
    except:
        print('\nPlease enter a number.')
        continue
    if useropt == 1:
        try:
            entrec(input('\nEnter Product Code: '),
            input('Enter Product Description: '),
            int(input('Enter value of Stock: ')))
        except:
            print('\nPlease enter an integer value for Stock')
    elif useropt == 2:
        disrec()
    elif useropt == 3:
        updstock(input('\nEnter the product code of the item that you want to update: '))
    elif useropt == 4:
        break
    else:
        print('\nPlease choose a number between 1 and 4')