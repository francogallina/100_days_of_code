alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
"""
def encrypt(plain_text, shift_amount):
    cipher_text=""
    for i in plain_text:
        position=alphabet.index(i)
        position+=shift_amount
        cipher_text+=alphabet[position]
    print(cipher_text)
    
def decrypt(plain_text,shift_text):
    cipher_text=""
    for i in plain_text:
        position=alphabet.index(i)
        position-=shift_text
        cipher_text+=alphabet[position]
    print(cipher_text)

if direction == "encode":
    encrypt(text,shift)
elif direction=="decode":
    decrypt(text,shift)
else:
    print("Opcion incorrecta")
"""

def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
        shift_amount*=-1
    for i in start_text:
        position=alphabet.index(i)
        new_position=position+shift_amount
        end_text+=alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")
    
caesar(text,shift,direction)







