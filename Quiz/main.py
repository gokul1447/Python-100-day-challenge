from quiz import Quiz
from data import qns



for i in range(len(qns)):
    current_qn=qns[i]["question"]
    answer=qns[i]["correct_answer"]
    qnum=i+1

    quiz=Quiz(current_qn,answer,qnum)

    quiz.choose_ans() 
    
        

    


