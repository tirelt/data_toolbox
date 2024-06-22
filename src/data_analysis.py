import numpy as np
import pandas as pd

def check_data(df):
    nbre_entries = df.shape[0]
    unique_value_col = []
    type_summary_col = []
    count_nan_col = []
    for col in df.columns:
        my_series = df[col]
        type_summary_col.append(get_type_summary(my_series))
        unique_value_col.append(np.round(nbre_unique_value(my_series)/nbre_entries*100,2))
        count_nan_col.append(np.round(count_nan(my_series)/nbre_entries*100,2))

    array = np.concatenate((np.array([df.columns.values]).T,np.array([count_nan_col,unique_value_col,type_summary_col],dtype=object).T),axis=1)
    df_analysis = pd.DataFrame(data=array,columns = ["Feature","NaN","Unique","Type"])
    return df_analysis

def count_nan(my_series):
    return np.sum(my_series.isnull().values)

def nbre_unique_value(my_series):
    return len(set(my_series))

def get_type_summary(my_series):
    type_series = my_series.apply(type)
    type_summary = []
    types = set(type_series)
    for _type in types:
        nbre = np.sum((type_series == _type).values)
        type_summary.append((_type,nbre))
    return type_summary