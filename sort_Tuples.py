def last(n):
    return n[-1]

def sort_Tuples(item):
    return sorted(item, key=last)
print(sort_Tuples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))