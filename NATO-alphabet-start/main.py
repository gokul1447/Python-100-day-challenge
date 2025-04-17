# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass



import pandas as pd

data = pd.read_csv(r'C:/Programming/python/100 Days Python chlng/NATO-alphabet-start/nato_phonetic_alphabet.csv')
import numpy
print(numpy.__file__)


dic=data.to_dict()

new_dic = {row.letter: row.code for  (index, row) in data.iterrows()}
# print(new_dic)
word= input("Enter the name :  ").upper()
new_list=[new_dic[i] for i in word]
print(new_list)