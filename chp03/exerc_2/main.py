def print_twice(value : str) :
    print(value)
    print(value)

def do_twice(f, value) :
    f(value)
    f(value)

do_twice(print_twice, 'spam')

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

do_four(print_twice, 'spam')