i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}",end="\t")
        j += 1
        if j > i:
            print()
    i += 1