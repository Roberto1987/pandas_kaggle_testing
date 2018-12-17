import pandas as pd
from utilities import *

from pre_processing import *
from visualization import *

t_drugs_location = 'C:\\Users\\rtesta\\Documents\\z -Personal\\ML_drug_test\\drugsComTest_raw.csv'
t_drugs = pd.read_csv(t_drugs_location)
vertical_print(list(t_drugs.columns))
field_variety(t_drugs['drugName'])

cond_dict = process_conditions(t_drugs)
cond_dict = data_pruning(cond_dict,25)
simple_plot(cond_dict)
pie_chart(cond_dict)