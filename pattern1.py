def pattern1(n):
    m = 2 * n - 2
    for i in range(0, n):
        for j in range(0, m):
            print(end=" ")
        m = m - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
n = 5
pattern1(n)
