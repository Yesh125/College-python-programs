num=int(input("Enter a number : ")) 
temp=num 
res=0 
while num>0: 
    remainder=num%10 
    res=res*10+remainder 
    num=num//10 
    if res==temp: 
        print("Number is Palindrome") 
    else: 
        print("Number is not Palindrome")

