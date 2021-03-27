def FizzBuzz(number):
    # Nombre égal ou inférieur à 0, retourne une erreur
    if number <= 0:
        raise ValueError

    # Nombre multiple de 3 et 5, retourne FizzBuzz
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"

    # Nombre multiple de 3, retourne Fizz
    if number % 3 == 0:
        return "Fizz"

    # Nombre multiple de 5, retourne Buzz
    if number % 5 == 0:
        return "Buzz"