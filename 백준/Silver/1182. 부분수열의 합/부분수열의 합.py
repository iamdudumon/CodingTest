def sum_recursive(idx, sum, size):
    temp = 1 if sum == s and size != 0 else 0

    if idx >= n:
        return temp
    else:
        return sum_recursive(idx + 1, sum + sequence[idx], size + 1) + sum_recursive(idx + 1, sum, size)

n, s = map(int, input().split())
sequence = list(map(int, input().split()))

print(sum_recursive(1, sequence[0], 1) + sum_recursive(1, 0, 0))