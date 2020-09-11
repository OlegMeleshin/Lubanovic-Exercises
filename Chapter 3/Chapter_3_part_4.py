# 10. Create an English-French dictionary called "e2f" and print it.
# Here are your words: dog/chien, cat/chat and walrus/morse.

e2f = {'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}
print(f'''English to French Dictionary
{e2f}\n''')



# 11. Print french for walrus using your dictionary.

print(f"French for walrus is {e2f['walrus']}\n")



# 12. Create French-English dictionary based on e2f dictionary using
# "items" method.

f2e = {}
for key in e2f:
    f2e[e2f[key]] = key
print(f'''French to English Dictionary
{f2e}\n''')



# 13. Print English word for "chien".

print(f'''Chien is a French word for {f2e['chien']}\n''')



# 14. Create and print a set of English words of e2f dictionary

eng_words = set(list(e2f.keys()))
print(f"Set of English words:\n{eng_words}")







