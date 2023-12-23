def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Dzielenie przez zero jest niedozwolone.")
    return a / b

if __name__ == "__main__":
    num1 = 10
    num2 = 5

    print(f"Dodawanie: {add_numbers(num1, num2)}")
    print(f"Odejmowanie: {subtract_numbers(num1, num2)}")
    print(f"Mnożenie: {multiply_numbers(num1, num2)}")
    
    try:
        print(f"Dzielenie: {divide_numbers(num1, num2)}")
    except ValueError as e:
        print(f"Błąd: {e}")
