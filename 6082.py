import sys

num = int(sys.stdin.readline())
for i in range(1, num + 1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 ==9:
        print("X")
    else:
        print(i)

