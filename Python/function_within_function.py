a=[1,2,3,4]

def add(a):
    def sum1():
        s=0
        for i in a:
            s=s+i
        return s
    return sum1

var=add(a)
print(var())

def add(a):
    def sum1():
        s=0
        for i in a:
            s=s+i
        return s
    return sum1()

var=add(a)
print(var)
# print(var())

def add1(a):
    def mul():
        s=1
        for i in a:
            s=s*i
        def add():
            s=0
            for i in a:
                s=s+i
            return s
        return s,add()
    return mul()
print(add1(a))
