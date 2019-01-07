import statistics as s

from pandas import DataFrame

from utilities import dict_check


def estimators(dataset):
    dict_check('estimators', dataset)
    print('Mean: {}, Variance: {} '.format(
        s.mean(dataset.values()),
        s.stdev(dataset.values(), s.mean(dataset.values()))
    )
    )
    print('Median: {}'.format(s.median(dataset.values())))
    print('Mode: {}'.format(s.mode(dataset.values())))


# noinspection PyBroadException
def process_conditions(dataset: DataFrame):
    conditions = list(dataset['condition'].unique())
    conditions_instances = {}
    for i in conditions:
        try:
            # print('Drug name: {}, instances: {}'.format(i,len(t_drugs[t_drugs['condition'] == i])))
            conditions_instances[i] = len(dataset[dataset['condition'] == i])
        except:
            print('row {} not correctly elaborated'.format(i))
    estimators(conditions_instances) # Printing some estimators
    return conditions_instances


# dictionary type user
def data_pruning(dataset, threshold):
    print('Threshold: {} '.format(threshold))
    dict_check('data_pruning', dataset)
    pruned = {}
    for i in dataset:
        if dataset[i] >= threshold:
            pruned[i] = dataset[i]
            print(dataset[i])
    print('{} has been pruned'.format(len(dataset) - len(pruned)))
    return pruned


def percentage(dataset: dict):
    dict_check('percentage', dataset)
    tot = sum(list(dataset.values()))
    for i in dataset:
        dataset[i] = dataset[i] / tot * 100
        # print(dataset[i])
    return dataset
