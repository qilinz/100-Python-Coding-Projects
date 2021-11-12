# A prime checker function
def prime_checker(number):
    is_prime = True
    # take care of exception
    if number <= 0:
        print("Please enter a positive number.")
    elif number <= 2:
        print("It's a prime number.")
    else:
        # prime check
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
        if is_prime:
            print("It's a prime number.")
        else:
            print("It's not a prime number")


# call the function
n = int(input("Check this number: "))
prime_checker(number=n)
