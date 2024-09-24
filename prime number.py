num=int(input("Enter the number:"))
if num>1:
    for i in range(2,num):
        if(num%i==0):
            print(num, "it is not a prime number")
            break
    else:
        print(num, "its a prime number")
else:
    print(num, "not a prime number")
    
