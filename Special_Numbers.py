number = int(input())

for i in range(1, number+1):
    digit = 0
    char = str(i)
    for a in char:
        digit += int(a)
    if digit == 5 or digit == 7 or digit == 11:
        print(f"{i} -> True")
    else:
        print(f"{i}-> False")
