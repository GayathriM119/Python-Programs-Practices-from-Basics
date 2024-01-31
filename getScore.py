def getScore(name,score,dept):
    return score/10


def main():
    name=input("Enter Your Name:")
    score=int(input("Enter your score for 100: "))
    dept=input("Enter your department: ")
    result=getScore(name,score,dept)
    print("My Name is: ",name)
    print("My Score is: ",result,"/10")
    print("My Department is: ",dept)

main()
    
