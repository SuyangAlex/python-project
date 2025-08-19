def get_largest(item):
    largest = 0
    for n in item:
        if n > largest:
            largest = n
    return largest
print(get_largest([2, 4,6,7,22,43,22,31,-25]))