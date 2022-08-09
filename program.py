a = int(input('Enter a first number : '))
b = int(input('Enter a second number : '))
c = int(input('Enter a third number : '))

def give_remainder_dict(a,b,c):
    div = a/b
    t = (f'%.{c}f' % (div))
    frac = float(t) % 1
    frac = str(frac)
    frac = frac[2:c+2]
    d = {}
    for i in range(0,10):
        d[i] = frac.count(str(i))
    print(d)

give_remainder_dict(a,b,c)