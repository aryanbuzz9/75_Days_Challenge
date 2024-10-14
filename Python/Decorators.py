def get_age(age):
    def get_name(name):
        return 'The '+name+' age is '+str(age)
    return get_name

var=get_age(21)
# print(var('aryan'))

def add(a):

    return sum(a)
a=[1,2,3,4]
# print(add(a))
