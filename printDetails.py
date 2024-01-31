def PrintData(name,age,address):
    print("My Name is: ",name,"\n")
    print("My Age is: ",str(age),"\n")
    print("My Address is: ",address,"\n")
def Main():
    name=input("Enter Your Name: ")
    age=int(input("Enter Your Age: "))
    address=input("Enter Your Address: ")
    PrintData(name,age,address)
    
Main()
