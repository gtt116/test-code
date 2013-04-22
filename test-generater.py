def inner():
    for i in range(1, 11):
        yield i


def outer():
    for i in inner():
        print i * i
        yield i


gen = outer()
print type(gen)
print gen

print gen.next()
print gen.next()
