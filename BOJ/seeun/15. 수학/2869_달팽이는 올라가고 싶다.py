a, b, v = map(int, input().split())

if a>=v:
    print(1)
else:
    if (v-a)%(a-b):
        print((v-a)//(a-b)+2)
    else:
        print((v-a)//(a-b)+1)
