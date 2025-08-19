# def remove_duplicates(lst):
#     for n in lst[:]:
#         if lst.count(n) > 1:
#             lst.remove(n)
#     return lst
# print(remove_duplicates([10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40, 10, 20]))

def remove_duplicates(lst):
    result = []
    for n in lst:
        if n not in result:
            result.append(n)
    result.sort()
    return result
print(remove_duplicates([10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40, 10, 20]))