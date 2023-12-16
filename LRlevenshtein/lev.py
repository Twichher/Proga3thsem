def score_lev(s1, s2):
    m, n = len(s1), len(s2)
    matrix = [[0] * (m+1) for i in range(n + 1)]

    for i in range(m+1):
        matrix[0][i] = i
    
    for j in range(n+1):
        matrix[j][0] = j

    for t1 in range(n+1):
        print(matrix[t1])

    for j in range(1, n+1):
        for i in range(1, m+1):
            if s2[j-1] == s1[i-1]:
                c = 0
            else:
                c = 1
            matrix[j][i] = min(matrix[j][i-1] + 1, matrix[j-1][i] + 1, matrix[j-1][i-1] + c)

    print("- " * (n+1))
    
    for t1 in range(n+1):
        print(matrix[t1])

    print("- " * (n+1))

    return matrix[n][m]


s1 = input()
s2 = input()
while(len(s1) == 0 or len(s2) == 0):
    print("error")
    s1 = input()
    s2 = input()

print(score_lev(s1, s2))

