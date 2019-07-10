import secrets
smaller = list(map(int,input().split()))

while True:
    a=secrets.choice(smaller)
    b=secrets.choice(smaller)

    if a+b==40:
        smaller.remove(a)
        smaller.remove(b)

        break

realSmaller=sorted(smaller)

for i in realSmaller:
    print(i)