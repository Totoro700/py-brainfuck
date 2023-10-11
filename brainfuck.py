def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_closest_factors(number):
    closest_factors = (1, number)
    min_difference = number - 1
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            other_factor = number // factor
            difference = abs(factor - other_factor)

            if difference < min_difference:
                min_difference = difference
                closest_factors = (factor, other_factor)
    return closest_factors

RESET = "[-]"

def setPointer(ascii):
    if is_prime(ascii):
        factor1, factor2 = find_closest_factors(ascii - 1)
        extra_number = 1
        final = ">"
        for i in range(factor1):
            final += "+"
        final += "[-<"
        for i in range(factor2):
            final += "+"
        final += ">]<"
        for i in range(extra_number):
            final += "+"
        final += f".{RESET}"
        return final
    else:
        factor1, factor2 = find_closest_factors(ascii)
        final = ">"
        for i in range(factor1):
            final += "+"
        final += "[-<"
        for i in range(factor2):
            final += "+"
        final += f">]<.{RESET}"
        return final
    
while True:
    toBrainfuck = input(": ")
    toBrainfuckAscii = []
    for char in list(toBrainfuck):
        toBrainfuckAscii.append(ord(char))
    FINAL = ""
    for ascii in toBrainfuckAscii:
        FINAL += setPointer(ascii)
    print(FINAL)