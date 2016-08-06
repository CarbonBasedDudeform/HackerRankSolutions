def f(x, e):
    new = ""
    for l in x:
        new += str((int(l)+e) % 10)

    return new

x = input()
e = int(input())
print(f(x,e))
