# Dragons and Wizards
print("Welcome to Dragons and Wizards.")

# Number of times the card is drawn
n = int(input("How many times would you like to draw the cards? "))

# Declaring scores
d_point = 0
w_point = 0

# Drawing Cards
for i in range(n):
    shape = str(input("\nEnter Shape: (Hearts, Spades, Diamonds, Clubs)\n"))
    
    # Hearts and its number
    if shape == 'Hearts':
        heartval = 0
        inttry = 0
        while inttry == 0:
            enterint = input("Do you want to draw a Heart with a number? (y/n) ")
            if enterint == 'y':
                heartval = int(input("Enter number for Hearts: "))
                break
            elif enterint == 'n':
                break
            else:
                print('\nPlease enter a valid answer!')
      
    if shape == 'Hearts' and heartval > 0:
        w_point += 1
        print('\nOne point to the Wizards!', d_point, '-', w_point)
    
    elif shape == 'Spades':
        w_point += 1
        print('\nOne point to the Wizards!', d_point, '-', w_point)
    
    elif shape == 'Hearts':
        d_point += 1
        print('\nOne point to the Dragons!', d_point, '-', w_point)
    
    elif shape == 'Diamonds' or 'Clubs':
        d_point += 1
        print('\nOne point to the Dragons!', d_point, '-', w_point)
      
        
# Determining the winning team
if d_point > w_point :
    print("\nTeam Dragons win!", d_point, "-", w_point)
elif d_point == w_point:
    print("\nIt's a Tie!", w_point, "-", d_point)
else:
    print("\nTeam Wizards win!", w_point, "-", d_point)
