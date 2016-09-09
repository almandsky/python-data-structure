from itertools import zip_longest
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

longest_name = None
max_letters = 0

'''
for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
from itertools import zip_longest
'''
'''
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count
'''
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
                
print(longest_name)

names.append('Rosalind')
'''
for name, count in zip(names, letters):
    print(name)
'''
for name, count in zip_longest(names, letters):
    print(name)

