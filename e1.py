n = input()
b = ''
c = 0
for i in range(len(n)+c):
    if i % 3 != 0:
        b += n[i]
print(b)
