
# Check if the value is of dict type
def dict_check(func_name, var):
    if type(var) is not dict: raise TypeError(
        '{} requires a dict as input: you inserted a {}'.format(var, type(var)))


def spacing(n=10):
    for i in range(0, n):
        print('-', end='')
    print()


def vertical_print(x):
    spacing()
    for i in x:
        print(i)
    spacing()


def field_variety(x):
    spacing()
    print(x.name)
    spacing()
    print(len(x.unique()))
    spacing()


def extract_threshold(dataset):
    pass
