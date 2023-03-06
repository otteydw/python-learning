import sys
p=0
a=None
for n in [int(x) for x in sys.argv[1].split(',')]:
    if n == p + 2:
        a = n - 1
    else:
        p = n
print(a)
