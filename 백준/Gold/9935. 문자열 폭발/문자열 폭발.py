import sys

input = sys.stdin.readline

ss = input().strip()
bomb = input().strip()
stack = []

def is_bomb(stack, bomb):
	if len(stack) < len(bomb):
		return False
	for i, ch in enumerate(stack[-len(bomb):]):
		if bomb[i] != ch:
			return False
	return True

for ch in ss:
	stack.append(ch)
	if is_bomb(stack, bomb):
		for _ in bomb:
			stack.pop()

answer = "".join(stack)
print(answer if answer else "FRULA")
