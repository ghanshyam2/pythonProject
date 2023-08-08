def fib(n):
    if n <= 1:
        return n
    return n * fib(n - 1)


print(fib(5))
print(fib(4))
