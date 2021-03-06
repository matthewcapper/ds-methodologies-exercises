import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

def peekatdata(df):
    '''gives cursory sample of dataframe passed'''
    head_df = df.head(5)
    print(head_df)
    tail_df = df.tail(5)
    print(tail_df)
    shape_tuple = df.shape
    print(shape_tuple)
    describe_df = df.describe()
    print(describe_df)
    df.info()

def encode_gender(df):
    '''encodes gender column into a new enumerated column'''
    encoder=LabelEncoder()
    encoder.fit(df.gender)
    return df.assign(gender_e = encoder.transform(df.gender))

def remove_numerical_outliers(df):
    '''Parses any numerical columns and removes outliers based on inner quartile range.'''
    for col in df:
        if np.issubdtype(df[col].dtype, np.number):
            q1 = float(df[[col]].quantile(.25))
            q3 = float(df[[col]].quantile(.75))
            iqr = q3 - q1
            df = df[~(df[col] > (q3 + 1.5 * iqr)) & ~(df[col] < (q1 - 1.5 * iqr))]
    return df



def show_numerical_outliers(df):
    '''Parses any numerical columns and removes outliers based on inner quartile range.'''
    for col in df:
        if np.issubdtype(df[col].dtype, np.number):
            q1 = float(df[[col]].quantile(.25))
            q3 = float(df[[col]].quantile(.75))
            iqr = q3 - q1
            if df[(df[col] > (q3 + 1.5 * iqr)) | (df[col] < (q1 - 1.5 * iqr))].empty:
                print(f'No outliers in {col}')
            else:
                print(f'OUTLIERS FOR {col}: \n')
                print(df[(df[col] > (q3 + 1.5 * iqr)) | (df[col] < (q1 - 1.5 * iqr))])


def prep_mall_data(df):
    '''pipes all but drop_cols and value_counts to groom our initial dataset'''
    return encode_gender(df)