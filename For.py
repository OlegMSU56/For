numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
numbers.pop(0)  # убираем 1 из списка так как это и не простое и не составное число

for i in numbers:
    is_prime = True  # допустим число простое
    for j in range(2, i):
        if i % j == 0:  # если остаток деления равен 0
            is_prime = False  # если остаток деления не равен 0 то число простое
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print('Prime :', primes)
print('Not Primes :', not_primes)






