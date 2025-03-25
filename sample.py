# user_text=input("Type the text: ")
# shift=int(input("Type shift number: "))
# alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")


# def encodein(shift_num , text):
     
#      new_text = ''
#      text=text.lower()
#      for i in text:
          
          
#           new_index = alphabet.index(i) + shift_num
#           if new_index > 25:
#                new_index = new_index - 26
#           new_text += alphabet[new_index]
#      print(new_text)     
   
# encodein(shift_num = shift,text=user_text)

# text=input("Type the decoded text : ")

# shift_num=int(input("Type shift number: "))
# alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

# def decodein(shift_num,text):
#      og_text=''
#      text=text.lower()
#      for i in text:
#           new_index=alphabet.index(i) - shift_num
#           if new_index < 0:
#                new_index += 26
#           og_text += alphabet[new_index]
          
#      print(og_text)     

# decodein(shift_num,text) 
data=[{'name':'gokul'},{'name':'rahul'}]
b='name'
a=data[0][b]

print(a)


      

