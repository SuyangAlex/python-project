def vowel(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for i in s:
 	    if i not in vowels:
            continue
        else:
            count += 1
    return count

fruit = ['apple', 'pear', 'kiwi']
sorted_fruit = sorted(fruit, key = vowel)
print(sorted_fruit)
