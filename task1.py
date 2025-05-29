even_n = sum (i for i in range(100, 1001) if i % 2 == 0)
odd_n = sum (i for i in range(100, 1001) if i % 2 != 0)
print(f"Сумма четных чисел: {even_n}, Сумма нечетных чисел: {odd_n}")