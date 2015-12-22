throwaway = input()
data = input()
data = data.split()
data = list(map(int, data))

myMap = {}
for x in range(1, len(data)+1):
    myMap[x] = data[x-1]

ans = "YES"
for x in range(1, len(data)+1):
    y = myMap[x]
    if (myMap[y] != x):
        ans = "NO"
        break

print(ans)
