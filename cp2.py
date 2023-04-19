alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(plain_text,shift_amount,caeser_operation):
    end_text=""
    if caeser_operation=="decode":
         shift_amount *=-1
    shift_amount %=26
    for letters in plain_text:
        if letters.isalpha():
            position=alphabet.index(letters)
            
            new_position=position+shift_amount
            new_letter =alphabet[new_position]
        else: 
            new_letter =letters
        end_text +=new_letter
    print(f"The {caeser_operation}d is {end_text}")
    
while True:   
    text=input("your text\n")
    shift=int(input("shift number:\n"))
    operation=input("encode or decode").lower()
    caeser(plain_text=text,shift_amount=shift,caeser_operation=operation)
    result=input("type yes to continue and no to exit").lower()
    if result=="no":
        break
