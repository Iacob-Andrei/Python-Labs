import sympy


def process_item(x: int) -> int:
    while True:
        x += 1
        if sympy.isprime(x):
            return x


if __name__ == '__main__':
    try:
        inp = int(input("Give input for function: "))
        print(process_item(inp))
    except ValueError as e:
        print("Wrong input", e)

