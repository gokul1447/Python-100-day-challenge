points=0
class Quiz:
    def __init__(self,qn,answer,qnum):
        
        self.qns=qn
        self.answers=answer
        self.current_qn=qnum
        
        


    
    def choose_ans(self):
        global points
      
        answ=input(f"{self.qns} Type True/False ")
        
        if answ==self.answers :
            
            points+=1
        print(f"your score is {points} out of {self.current_qn}")
    
    
        
        
    

        