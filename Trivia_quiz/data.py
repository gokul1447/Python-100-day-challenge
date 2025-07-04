import requests
import random

class Datas:
    def __init__(self):
        self.qns=[]
      
        
        self.response=requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
        self.data=self.response.json()

   
    def question(self):
        for i in self.data["results"]:
            self.qns.append((i["question"],i["correct_answer"]))
    def getQn(self):
        self.question()
        choise=random.randint(1,10)
        return self.qns[choise]

        
        



