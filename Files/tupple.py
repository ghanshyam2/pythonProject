def tuple_fun(lis, lisFun):
    list_fun = zip(lis, lisFun)
    res = set(list_fun)

    return res


print(tuple_fun([2, 3, 4, 5, 6, 7], [4, 6, 8, 10, 12,14]))
