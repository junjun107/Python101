alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

def encrypt(user_text,shift_amount):
    # print(user_text,shift_amount)
    cipher_text = ""
    for i in user_text:
       textIndex = alphabet.index(i)
       newTextIndex = textIndex+shift_amount
       # print(newTextIndex)
       newLetter=alphabet[newTextIndex]
       cipher_text+=newLetter
    # print(cipher_text)

encrypt(text,shift)

def decrypt(cipher_text,shift_amount):
    plain_text=""
    for i in cipher_text:
       position = alphabet.index(i)
       new_position = position - shift_amount
       plain_text += alphabet[new_position]
    print(f"The encoded text is {plain_text}")
decrypt(text,shift)

if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)