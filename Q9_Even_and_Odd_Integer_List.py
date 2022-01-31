# Program to determine whether the number of odd and even digits in a list are equal

def balanced(a):
    if a == '':
        print("True")
    else:   
        int_list = []
        for i in str(a):
            int_list.append(int(i))

        even_count = 0
        odd_count = 0
        
        for i in int_list:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        print(odd_count == even_count)
        

balanced(input("Enter the integers you want to compare: "))
