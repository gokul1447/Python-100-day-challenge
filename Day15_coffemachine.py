menu={
    "espresso":{
        'ingredinents':{
            'water':50,
            'coffee':18,
            
        },
        "cost":150,

         

    },

    "latte":{
        'ingredinents':{
            'water':200,
            'coffee':20,
            'milk':100
            
        },
        "cost":250,

         

    },

    "cappuccino":{
        'ingredinents':{
            'water':150,
            'coffee':30,
            'milk':150,
            
        },
        "cost":350,

         

    },
        
}
resourse={"water":300,
          'milk':200,
          
          'coffee':100,}
cont='y'
while cont=='y':
   
    reply=input("what would you like? (espresso/latte/cappuccino)")
    b=1
    def money(reply):
        rs=int(input("please insert coins: "))
        if reply=='1':
            if resourse['water']<menu['espresso']['ingredinents']['water'] or resourse['coffee']<menu['espresso']['ingredinents']['coffee']:
                 
                    return f"{rs} Stocks finished"

            elif rs<150 :

                
                b=0
                return 'not enough'
               
            elif rs>=150:
                print("Here is your espresso, enjoy")

                return rs-150 
        elif reply=='2':
            if resourse['water']<menu['latte']['ingredinents']['water'] or resourse['milk']<menu['latte']['ingredinents']['milk'] or resourse['coffee']<menu['latte']['ingredinents']['coffee'] :
                return f"{rs} Stocks finished"


            elif rs<250 :
                
                
                b=0
                return 'not enough'

                
            elif rs>=250:
                print("Here is your latte, enjoy")
                return rs-250 
        elif reply=='3':
            if resourse['water']<menu['cappuccino']['ingredinents']['water'] or resourse['milk']<menu['cappuccino']['ingredinents']['milk'] or resourse['coffee']<menu['cappuccino']['ingredinents']['coffee']   :
                    return f"{rs} Stocks finished"
            elif rs<350 :
                
                
                b=0
                return 'not enough'

                
            elif rs>=350:
                print("Here is your cappucino, enjoy")
                return rs-350      
        

    if (reply=='report'):
        print(resourse)
    elif reply=='1':
        print(f"Your balance is {money(reply)}")
        if b==0:
            print(" ")

        elif b==1: 
        
            resourse['water']-=menu['espresso']['ingredinents']['water']
        
            resourse['coffee']-=menu['espresso']['ingredinents']['coffee']
        
        
    elif reply=='2':
        print(f"Your balance is {money(reply)}")
        if b==0:
            print("nopeeee")

        elif  b==1: 
                   
            resourse['water']-=menu['latte']['ingredinents']['water']
            resourse['milk']-=menu['latte']['ingredinents']['milk']
            resourse['coffee']-=menu['latte']['ingredinents']['coffee']
            
    elif reply=='3':
        print(f"Your balance is {money(reply)}") 
        if b==0:
            print(" ")

        elif b==1: 
            resourse['water']-=menu['cappuccino']['ingredinents']['water']
            resourse['milk']-=menu['cappuccino']['ingredinents']['milk']
            resourse['coffee']-=menu['cappuccino']['ingredinents']['coffee']   
    else :
            exit()

  