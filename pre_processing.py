import statistics as s



# Taking a dictionary
from utilities import dict_check


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



# dictionary type user
def data_pruning(dataset, threshold):
    if type(dataset) is not dict: raise TypeError(
        'data_pruning requires a dict as input: you inserted a {}'.format(type(dataset)))
    pruned = {}
    for i in dataset:
        if dataset[i] > 6: pruned[i] = dataset[i]
    print('{} has been pruned'.format(len(dataset) - len(pruned)))
    return pruned
