# Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
# Output: [1, 2, 3]


def union_problem(a, b):
    c = set(a).union(set(b))

    return list(c)

print(union_problem([1, 2, 3, 2, 1], [3, 2, 2, 3, 3, 2]))
