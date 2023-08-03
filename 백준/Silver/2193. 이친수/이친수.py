n = int(input())

pinary_numbers = [0] * 91
pinary_numbers[1] = 1
pinary_numbers[2] = 1

for idx in range(3, n + 1):
    for j in range(idx - 2):
        pinary_numbers[idx] += pinary_numbers[idx - 2 - j]
    pinary_numbers[idx] += 1

print(pinary_numbers[n])