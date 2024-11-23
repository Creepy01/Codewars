def product_fib():
    Fib = [1, 1] + [Fib[i-1] + Fib[i-2] for i in range(2, 100)]
    return Fib
print(product_fib())