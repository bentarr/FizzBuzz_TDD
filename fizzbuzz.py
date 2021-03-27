def FizzBuzz(nombre):
    # Nombre égal ou inférieur à 0, retourne une erreur
    if nombre <= 0:
        raise ValueError

    # Nombre multiple de 3, retourne Fizz
    if nombre % 3 == 0:
        return "Fizz"

    # Nombre multiple de 5, retourne Buzz
    if nombre % 5 == 0:
        return "Buzz"

    # Nombre multiple de 3 et 5, retourne FizzBuzz
    if nombre % 3 == 0 and nombre % 5 == 0:
        return "FizzBuzz"