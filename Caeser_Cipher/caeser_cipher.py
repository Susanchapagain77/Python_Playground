
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caeser(plain_text, shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
            shift_amount *=-1
    
    shift_amount%=26
    for letters in plain_text:
        if letters.isalpha():
            position=alphabet.index(letters)
            new_position=position+shift_amount
            new_letter=alphabet[new_position]
        else:
            new_letter=letters
        end_text +=new_letter
            
    print(f"The {cipher_direction}d text is {end_text}")


  
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(plain_text=text,shift_amount=shift,cipher_direction=direction)
    
    
    result= input("Type yes to continue and No to exit the program\n").lower()
    if result=="no":
        break
