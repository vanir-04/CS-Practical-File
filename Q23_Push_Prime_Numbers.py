# Check for prime numbers and push into stack

def pushprimes(inlist):
    outlist = []
    isprime = False
    if 2 in inlist:
        outlist.append(2)
    for i in inlist:
        for dnm in range(2,int(i)):
            if int(i)%dnm != 0:
                isprime = True
            else:
                isprime = False
                break
        else:
            if isprime is True:
                outlist.append(i)
    global primestack
    primestack = outlist

primestack = []
numlist = []

while True:
    print('Current list:',numlist)
    useropt = input("Enter numbers to add to list (type a string to stop adding): ")
    try:
        num = int(useropt)
        numlist.append(num)
        continue
    except:
        break

pushprimes(numlist)

print('\nThe final stack is:')
print(*primestack, sep='\n')