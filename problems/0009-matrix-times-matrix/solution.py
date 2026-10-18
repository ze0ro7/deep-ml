def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> list[list[int | float]]:

    if not a or not b or len(a[0]) != len(b):
        return -1

    bt = list(zip(*b))
    c = [ [sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]

    return c