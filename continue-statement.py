# 1. continue using for loop

for i in range(1, 11):
    if i == 6:
        continue
    print(i)
    # 2. continue using while loop

i = 0

while i < 10:
    i = i + 1

    if i == 6:
        continue

    print(i)