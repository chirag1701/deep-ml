def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    b = []
    for i in range(len(a[0])):
        arr = []
        for j in range(len(a)):
            arr.append(a[j][i])
        b.append(arr)
    return b