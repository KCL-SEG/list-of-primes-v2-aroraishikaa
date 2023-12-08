def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be a positive integer")

    list_of_primes = []
    num = 2  # Starting from the first prime number

    while len(list_of_primes) < number_of_primes:
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            list_of_primes.append(num)
        num += 1

    return list_of_primes


