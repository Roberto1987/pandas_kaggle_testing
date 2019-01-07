import pandas as pd
from utilities import *

from pre_processing import *
from visualization import *

t_drugs_location = 'C:\\Users\\rtesta\\Documents\\z -Personal\\ML_drug_test\\drugsComTest_raw.csv'

t_drugs = pd.read_csv(t_drugs_location)

print(list(t_drugs.columns))

field_variety(t_drugs['uniqueID'])

# Get the number of all medical conditions in the data set

cond_dict = process_conditions(t_drugs)
cond_dict = percentage(cond_dict)

plt.figure(1)
simple_plot(cond_dict)

# Applying threshold of 3%
plt.figure(2)
cond_dict = data_pruning(cond_dict, 5)
simple_plot(cond_dict)

pie_chart(cond_dict)
plt.show()
