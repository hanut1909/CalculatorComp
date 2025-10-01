# gcd of two numbers

def gcd(a, b):
    result = min(a, b)

    while result > 0:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
    return result
