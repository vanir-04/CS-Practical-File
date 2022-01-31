# Program to simulate a Traffic Light

def LIGHT():
    # Declaring list of colours
    cols = ['RED', 'YELLOW', 'GREEN']
    
    # Letting the user select the colour of the light
    colchosen = False
    while colchosen == False:
        light = str(input("Enter the color of the traffic light: (RED, YELLOW, GREEN)\n"))
        if light.upper() not in cols:
            print(("Please choose a colour from the options given.\n"))
            continue
        else:
            colchosen = True
            break
    
    # Determining value from user's selection
    global val
    
    if light.upper() == 'RED':
        val = 0
    elif light.upper() == 'YELLOW':
        val = 1
    elif light.upper() == 'GREEN':
        val = 2

def trafficLight():
    # Calling LIGHT() function
    LIGHT()

    # Printing message based on value
    if val == 0:
        print("\nSTOP! Your life is precious!")
    elif val == 1:
        print("\nPlease WAIT until the light is GREEN!")
    elif val == 2:
        print("\nGO! Thank you for being patient!")

    # Printing message after trafficLight() has finished executing
    print("SPEED THRILLS BUT KILLS\n")

# Calling trafficLight() to begin program
trafficLight()