a = set()
n = int(input())

for i in range(2, int(n**0.5)+1):
    x = i*i
    while x <= n:
        a.add(x)
        x *= i
print(n - len(a))