n = int(input())
s = input()
alp = {chr(ord('a') + i) : i + 1 for i in range(26)}

sum = 0
for i, c in enumerate(s):
    sum += (alp[c] * 31**i)
print(sum % 1234567891)