"""
Fibonacci
"""


def main():
    n = int(input("How many Fibonacci numbers should I print?"))
    print(tuple(fib(n)))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    main()
