def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1,2,3))
# print(sum_all(1,2,3,55))
# print(sum_all(1,2,3,0,34,5,6,8,8,))