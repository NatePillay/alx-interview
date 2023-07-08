def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                previous_row = triangle[i - 1]
                current_row =  previous_row[j - 1] + previous_row[j]
                row.append(current_row)
        triangle.append(row)
    return triangle
