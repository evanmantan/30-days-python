# # with open('words.txt') as f:
# #     text = f.read()
# #     words = text.split('\n')

# # print(words)

# # for word in words:
# #     print(word)

# l = ['hey', 'there', '!']

# print(l)

# def hapus(a):
#     a.pop()

# hapus(l)
# print(l)

def conceal(word):
    distinct = []
    for i in word:
        if i not in distinct:
            distinct.append(i)
    return distinct

word = 'aaaabbbcc'
print(conceal(word))

remove