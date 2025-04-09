def matrix_dot_vector(a: list[list[int|float]],b: list[int|float]) -> list[int|float]:
    arr_new = []
    if len(a[0]) == len(b) :
        for i in range(len(a)):
            summ = 0
            for j in range(len(a[i])):
                summ+= a[i][j]*b[j]
            arr_new.append(summ)
        return arr_new
    else:
        return -1
