# String Rotation

def rotate_word():
    alphabegin = ord("a")
    alphaend = ord("z")
    inp_str = str(input("Enter the word you want to encrypt: "))
    num = int(input("Number of rotations: "))
    rot_num = num%26
    new_str = ''
    for i in inp_str.lower():
        new_num = ord(i) + rot_num
        while new_num > alphaend: 
            new_num -= 26
        while new_num < alphabegin: 
            new_num += 26
        new_str += chr(new_num)
    print(new_str)  
    
rotate_word()