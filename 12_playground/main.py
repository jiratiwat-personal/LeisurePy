def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

ans = add(1,2,3,4)
print(ans)