# Stacks Menu-driven Program

def MakePush(Package):
    PackageList.append(Package)

def MakePop():
    try:
        print('\nSuccessfully popped',PackageList.pop())
    except:
        print('\nStack is empty!')

def ShowList():
    print('\n__________\n')
    print(*PackageList[::-1], sep='\n')
    print('__________\n')

PackageList = []

while True:
    print('\n[1] Show stack\n[2] Push item to stack\n[3] Pop item from stack\n[4] Quit')
    try:
        useropt = int(input("\nSelect [1], [2], [3], or [4]: "))
    except:
        print('\nPlease enter a number.')
        continue
    if useropt == 1:
        ShowList()
    elif useropt == 2:
        MakePush(input("\nEnter package to push: "))
    elif useropt == 3:
        MakePop()
    elif useropt == 4:
        break
    else:
        print('\nPlease enter a value between 1 and 4')