# Check if the value is of dict type
def dict_check(func_name, var: dict):
    if type(var) is not dict: raise TypeError(
        '{} requires a dict as input: you inserted a {}'.format(var, type(var))
    )


def field_variety(x):
    print(x.name)
    print(len(x.unique()))


def extract_threshold(dataset):
    pass
