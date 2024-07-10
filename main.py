test_examples = [
    [0, 1, 0, 12, 3],
    [0],
    [1, 0, 13, 0, 0, 0, 5],
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
]

for example in test_examples:
    non_zero_lst = [x for x in example if x != 0]
    zero_count = example.count(0)
    result = non_zero_lst + [0] * zero_count
    print(example, '->', result)
