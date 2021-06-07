import django
from real_estate.dataset import Dataset
from real_estate.housing import Housing
import pandas as pd


if __name__ == '__main__':
    df = pd.DataFrame()
    while 1:
        m = input('1, 2, 3, 0\n'
                  '>> ')
        if m == '1':
            housing = Housing()
            housing.new_model()
            # df = pd.read_excel('./data/time_series_cost.xlsx')
        elif m == '2':
            housing.print_this(housing.new_model())
        elif m == '0':
            break
        else:
            continue
