# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 21:09:06 2022

@author: temel
"""

#Task 2: College data

import numpy as np
import pandas as pd

def read_file(in_name):
    out_data = pd.read_csv(in_name)
    
    return out_data

def replace_asterisks(in_data):
    if in_data == "*":
        return np.nan
    else:
        return in_data

data_set = read_file('usnews.csv')
data_set = data_set.applymap(replace_asterisks)
data_set.head(n=5)

def add_column(in_data):    
    in_data['Public_Private_Descr'] = np.where(in_data[['Public/private']]==1,'Public','Private')
    return in_data

data_set_2 = add_column(data_set)
data_set_2.head(5)

def interquartile(in_data, field_name_q1, field_name_q3, new_name):    
    Third_q = in_data[field_name_q3].factorize()[0]
    First_q = in_data[field_name_q1].factorize()[0]
    new_data = Third_q - First_q
    in_data[new_name] = new_data 
    return in_data

data_set_3 = interquartile(data_set_2,'First quartile - Math SAT','Third quartile - Math SAT','Interquartile - Math SAT')
data_set_4 = interquartile(data_set_3,'First quartile - Verbal SAT','Third quartile - Verbal SAT','Interquartile - Verbal SAT')
data_set_4.head()

def write_file(in_name,in_data):
    in_data.fillna("", inplace=True)
    in_data.to_csv(in_name, sep=',',index=False)
    return
write_file('usnews_processed.csv',data_set_4)


#Task 3: Unionized Workers

def read_file(in_name):
    out_data = pd.read_csv(in_name)
    return out_data

def control_flow_compute(in_file):
    total_wages = 0 
    union_count = 0
    average_union_wage  = 0
 
    for index, row in in_file.iterrows():
        if row["union"] == 'Union':
            total_wages += row["wage"]
            union_count += 1
    
    average_union_wage = total_wages / union_count
    return average_union_wage
        

data_set = read_file('cps.csv')
data_set.head(n=5)
control_flow_compute(data_set)

def return_row(in_row):
    if in_row["union"] == 'Union':
        return_val = in_row['wage']
    else:
        return_val = np.nan
    return return_val

def compute_row(in_panda):
    total_wages = 0 
    union_count = 0
    average_union_wage  = 0

    temp_panda = in_panda.apply(return_row, axis=1)
    for index, row in temp_panda.items(): 
        if row >= 0:
            total_wages += row
            union_count += 1
    
    average_union_wage = total_wages / union_count
    return average_union_wage
        
compute_row(data_set)

def union_calc(in_panda):
    return in_panda["wage"].mean(), in_panda["wage"] > 0

union_calc(data_set)

%time(control_flow_compute(data_set))
%time(compute_row(data_set))
%time(union_calc(data_set))

#Wall time: 58.8 ms
#Wall time: 12 ms
#Wall time: 996 us

%timeit(control_flow_compute(data_set))
%timeit(compute_row(data_set))
%timeit(union_calc(data_set))

#43.1 ms ± 4.35 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
#11.1 ms ± 1.16 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)
#244 us ± 10.9 us per loop (mean ± std. dev. of 7 runs, 1000 loops each)