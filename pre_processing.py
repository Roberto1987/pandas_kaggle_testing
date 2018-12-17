import statistics as s


# Check if the value is of dict type
def dict_check(func_name, var):
    if type(var) is not dict: raise TypeError(
        '{} requires a dict as input: you inserted a {}'.format(var, type(var)))


# Taking a dictionary
def estimators(dataset):
    dict_check('estimators',dataset)
    print('Mean: {}, Variance: {} '.format(
        s.mean(dataset.values()),
        s.stdev(dataset.values(), s.mean(dataset.values()))
    )
    )
    print('Median: {}'.format(s.median(dataset.values())))
    print('Mode: {}'.format(s.mode(dataset.values())))


# noinspection PyBroadException
def process_conditions(dataset):
    conditions = list(dataset['condition'].unique())
    conditions_instances = {}
    for i in conditions:
        try:
            # print('Drug name: {}, instances: {}'.format(i,len(t_drugs[t_drugs['condition'] == i])))
            conditions_instances[i] = len(dataset[dataset['condition'] == i])
        except:
            print('row {} not correctly elaborated'.format(i))
    estimators(conditions_instances)
    return conditions_instances


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


# dictionary type user
def data_pruning(dataset, threshold):
    if type(dataset) is not dict: raise TypeError(
        'data_pruning requires a dict as input: you inserted a {}'.format(type(dataset)))
    pruned = {}
    for i in dataset:
        if dataset[i] > 6: pruned[i] = dataset[i]
    print('{} has been pruned'.format(len(dataset) - len(pruned)))
    estimators(pruned)
    return pruned
