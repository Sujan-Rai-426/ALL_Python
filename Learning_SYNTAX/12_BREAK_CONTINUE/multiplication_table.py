for i in range(1,20):
    for j in range(1,20):
        print(i, " * ", j, " = ", i*j)
        if j==10:
            break
    if i==10:
        break