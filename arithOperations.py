def arithOp(a,b,c):
    mul1=a*b*c
    add1=a+b+c
    res=mul1/add1
    return res

def main():
    a=int(input("Enter number1: "))
    b=int(input("Enter number1: "))
    c=int(input("Enter number1: "))
    result=arithOp(a,b,c)
    print(a,"*",b,"*",c,"/",a,"+",b,"+",c,"=",result)
    
main()
