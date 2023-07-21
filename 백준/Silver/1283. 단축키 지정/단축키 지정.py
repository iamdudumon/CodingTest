n = int(input())

words = []
shortcit_keys = set()
answer = []

shortcit_keys.add(" ")

for i in range(n):
    word = input()
    words.append(word)

for i in range(n):
    word = words[i]
    word_split = word.split()

    #keep_goging = True
    temp_word = word
    temp_key = "null"

    for ch in word:
        if not shortcit_keys.__contains__(ch.upper()):
            temp_key = ch.upper()
            temp_word = word.replace(ch, "[" + ch + "]", 1)
            break

    for idx, word_item in enumerate(word_split):
        if not shortcit_keys.__contains__(word_item[0].upper()):
            temp_key = word_item[0].upper()
            word_split[idx] = word_item.replace(word_item[0], "[" + word_item[0] + "]", 1)

            temp_word = ""
            for str in word_split:
                temp_word += str + " "
                
            break
        
    shortcit_keys.add(temp_key)         
    answer.append(temp_word)

for item in answer:
    print(item)
 