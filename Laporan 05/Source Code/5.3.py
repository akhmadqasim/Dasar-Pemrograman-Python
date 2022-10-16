i = 1
while i < 100:
    if i % 3 == 0 and i % 7 == 0:
        print(i)
        break
    i += 1

for x in range(1, 100):
    if x %3 == 1:
        continue