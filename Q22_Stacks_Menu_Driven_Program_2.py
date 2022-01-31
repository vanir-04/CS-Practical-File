# Stacks Menu-driven Program 2

stack1 = []

def push(stk,item):
    stk.append(item)

def pop(stk):
    try:
        print('\nSuccessfully popped',stk.pop())
    except:
        print('\nStack is empty!')

def check(stk):
    if len(stk) != 0:
        print('\nStack is not empty.')
    else:
        print('\nStack is empty.')

def show(stk):
    print('\n__________\n')
    print(*stk[::-1], sep='\n')
    print('__________\n')

while True:
    print('\n[1] Show stack\n[2] Push item to stack\n[3] Pop item from stack\n[4] Check stack\n[5] Quit')
    try:
        useropt = int(input("\nSelect [1], [2], [3], [4], or [5]: "))
    except:
        print('\nPlease enter a number.')
        continue
    if useropt == 1:
        show(stack1)
    elif useropt == 2:
        push(stack1, input("\nEnter item to push to stack: "))
    elif useropt == 3:
        pop(stack1)
    elif useropt == 4:
        check(stack1)
    elif useropt == 5:
        break
    else:
        print('\nPlease enter a value between 1 and 5')