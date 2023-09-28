import math

def is_prime_number(n):
    if n <= 1:
        return False
    
    # Vérification de la divisibilité par les entiers de 2 à la racine carrée de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # Si aucun diviseur n'a été trouvé, le nombre est premier
    return True