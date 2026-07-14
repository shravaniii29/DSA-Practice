n = int(input("Enter a number: "))

if n <= 1:
    print("Invalid input. Please enter a number greater than 1.")

else:
    isPrime = True
    
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            isPrime = False
            break
        
    if isPrime:
            print(n, "is a prime number.")
            
    else:
        print(n, "is not a prime number.")
        