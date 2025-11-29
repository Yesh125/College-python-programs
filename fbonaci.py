n=int(input("How many fibonacci numbers to genearate : ")) 


def fib(n): 
    first=0 
    second=1 
    if n >= 1: 
        print(first, end=" ") 
        if n >= 2: 
            print(second, end=" ") 
            i=3 
            while i<=n: 
                third=first+second 
                print(third, end=" ") 
                first=second 
                second=third 
                i=i+1 
fib(n)