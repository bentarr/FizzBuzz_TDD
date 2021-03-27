def FizzBuzz(nombre):
    # Nombre égal ou inférieur à 0, retourne une erreur
    if nombre <= 0:
        raise ValueError

    # Nombre multiple de 3 , retourne Fizz
    if nombre % 3 ==0:
        return "Fizz"