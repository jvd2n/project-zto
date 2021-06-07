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
        return pd.read_excel(excel_dir
                                     , sheet_name='평균전세'
                                     )
