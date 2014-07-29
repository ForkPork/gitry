def func():
    for i in range(5):
        yield i * 5

list_i = func()
for j in list_i:
    print j
