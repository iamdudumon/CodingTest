from sys import stdin, stdout

input = stdin.readline;
write = stdout.write                                                                                                                                                                  
n, m = map(int, input().strip('\n').split())
poket_list = [input().strip('\n') for _ in range(n)]
poket_dict = {poket : i + 1 for i, poket in enumerate(poket_list)}

for _ in range(m):
    question = input().strip('\n')
    if question.isdigit():
        num = int(question)
        write(poket_list[num - 1] + '\n')
    else:
        write(str(poket_dict[question]) + '\n')