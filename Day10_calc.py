n1=int(input("whats the first number: "))
operator=input("+ \n* \n- \n/ \nType the operator: " )
n2=int(input("Type the 2nd number: "))
choice='n'
def oper(n1,n2,operator):
    if operator=='+':
        return n1+n2
    elif operator=='-':
        return n1-n2
    elif operator=='*':
        return n1*n2
    elif operator=='/':
        return n1/n2
    else:
        return "unknown operator"

result=(oper(n1,n2,operator))
print(f"{n1}{operator}{n2} = {result}")
choice=input("Type 'y' to contine calculating or 'n' to new calculation : ")
while choice=='y':
    n1=result
    operator=input("+ \n* \n- \n/ \nType the operator: " )
    n2=int(input("type 2nd number: "))
 
    result=(oper(n1,n2,operator))
    print(f"{n1}{operator}{n2} = {result}")
    choice=input("Type 'y' to contine calculating or 'n' to new calculation : ")





    

     

