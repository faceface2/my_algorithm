def wrapper(obj):
    print(obj)
    def inner(name, *args, **kwrags):
        if not obj.instance:
            obj.instance = obj(name)
        return obj.instance

    return inner


@wrapper
class Person(object):
    instance = None

    def __init__(self, name):
        self.name = name

    def printInfo(self):
        print(self.name)


zs = Person('张三')
zs.printInfo()
print(id(zs))

ls = Person('李四')
ls.printInfo()
print(id(ls))
