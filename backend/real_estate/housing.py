from real_estate.dataset import Dataset
import numpy as np
import pandas as pd
import os


class Housing(object):

    dataset = Dataset()

    def new_model(self) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = 'time_series_cost.xlsx'
        excel_dir = os.path.join(this.context, this.fname)
        this.housing = pd.read_excel(excel_dir
                                     , sheet_name='평균전세'
                                     )
        return this

    @staticmethod
    def print_this(this):
        print('*' * 100)
        print(f'1. Housing 의 type\n {type(this.housing)}')
        print(f'2. Housing 의 column\n {this.housing.columns}')
        print(f'3. Housing 의 상위 5개 행\n {this.housing.head(5)}')
        print(f'4. Housing 의 null 의 개수\n {this.housing.isnull().sum()}')
        print('*' * 100)
