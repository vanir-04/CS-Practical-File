# Program to find the frequency of  values in a given dictionary
 
D = {'P1':60,'P2':30,'P3':50,'P4':60,'P5':30,'P6':10}
newdict = {}

for i in D.values():
    if i in newdict:
        newdict[i] += 1
    else:
        newdict[i] = 1

print(newdict)