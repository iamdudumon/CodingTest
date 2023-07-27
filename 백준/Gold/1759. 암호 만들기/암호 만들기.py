def make_code(code, idx):
    if len(code) == l:
        vowel_count = 0
        for ch in code:
            if ch in vowel:
                vowel_count += 1
        if vowel_count > 0 and len(code) - vowel_count > 1:
            code_list.append(code)
        return;
    
    if idx < len(alphabet):
        make_code(code + alphabet[idx], idx+1)
        make_code(code, idx + 1)

l, c = map(int, input().split())
alphabet = sorted(input().split())
code_list =[]
vowel = set(['a', 'e', 'i', 'o', 'u'])

make_code("", 0)
for code in code_list:
    print(code)