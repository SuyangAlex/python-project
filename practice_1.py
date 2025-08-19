def count_string(item):
    count = 0
    for n in item:
        if n[0] == n[-1]:
            count += 1
    return count
print(count_string(['abc', 'xyz', 'aba', '1221', '15821']))