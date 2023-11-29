def pascal_triangle(n):
    triangle = []

    if (n == 0):
        return triangle

    triangle.append([1])

    for i in range(1, n):
        arr = [1]

        for j in range(1, i):
            arr.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        arr.append(1)
        triangle.append(arr)

    return triangle
