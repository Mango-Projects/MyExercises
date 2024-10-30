rows_A, cols_A = map(int, input().split())
A = [[*map(int, input().split())][:cols_A] for _ in range(rows_A)]

rows_B, cols_B = map(int, input().split())
B = [[*map(int, input().split())][:cols_B] for _ in range(rows_B)]

if (cols_A != rows_B):
    print("error")
else:
    C = [[0] * cols_B for _ in range(rows_A)]

    for x in range(rows_A):
        for y in range(cols_B):
            for z in range(cols_A):
                C[x][y] += A[x][z] * B[z][y]
    
    print("\n".join(" ".join(map(str, row)) for row in C))