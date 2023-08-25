n = int(input('enter number: '))
res = 0
while n >= 1000:
    res += n % 10
    n //= 10

res1 = 0
while n >= 1:
    res1 += n % 10
    n //= 10

if res == res1:
    print('yes')
else:
    print('no')