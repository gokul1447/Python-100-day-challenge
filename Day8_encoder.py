# Select encoding or decoding method
method = input("Select 1 if you need to encode\nSelect 2 if you need to decode\n")
a=input("hello")
# Define the alphabet as a string
alphabet = "abcdefghijklmnopqrstuvwxyz"

def encoder(shift_num, text):
    new_text = ''
    text = text.lower()

    for i in text:
        if i in alphabet:  # Ignore spaces and special characters
            new_index = (alphabet.index(i) + shift_num) % 26
            new_text += alphabet[new_index]
        else:
            new_text += i  # Keep spaces and special characters unchanged

    print("Encoded text:", new_text)    

def decoder(shift_num, text):
    og_text = ''
    text = text.lower()

    for i in text:
        if i in alphabet:
            new_index = (alphabet.index(i) - shift_num) % 26
            og_text += alphabet[new_index]
        else:
            og_text += i

    print("Decoded text:", og_text)     

if method == "1":
    user_text = input("Type the text: ")
    shift = int(input("Type shift number: "))
    encoder(shift_num=shift, text=user_text)

elif method == "2":
    text = input("Type the encoded text: ")
    shift = int(input("Type shift number: "))
    decoder(shift_num=shift, text=text)

else:
    print("Invalid option! Please select 1 or 2.")
