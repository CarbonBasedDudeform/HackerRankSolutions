inp = input()
new = ""
for x in inp:
    new += str((int(x) + 1) % 10)
print(new)
