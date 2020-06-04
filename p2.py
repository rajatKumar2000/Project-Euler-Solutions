fibonacci = [1,2]
sum = 2

while fibonacci[-1] + fibonacci[-2] < 4000000:
    next_term = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_term)

    if (next_term % 2 == 0):
        sum += next_term

print(sum)