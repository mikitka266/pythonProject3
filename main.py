def uniq(numbers: list):
    result = []
    double = []
    for i in numbers:
        if i not in result:
            result.append(i)
        else:
            double.append(i)
    return (result, double)


numb = [1, 3, 5, 5, 5, 5, 7, 8, 23, 32323, 2, 3, 3]

print(f'result list {uniq(numb)} double ')
