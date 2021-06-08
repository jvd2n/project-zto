from real_estate.services import HousingService
from real_estate.models import HousingDTO
import pandas as pd
import xlwings as xw


class HousingApi(object):

    @staticmethod
    def print_this(this):
        print('*' * 100)
        print(f'1. Housing 의 type\n {type(this)}')
        print(f'2. Housing 의 column\n {this.columns}')
        print(f'3. Housing 의 상위 5개 행\n {this.head()}')
        print(f'4. Housing 의 null 의 개수\n {this.isnull().sum()}')
        print('*' * 100)

    @staticmethod
    def main():
        util = HousingService()
        dto = HousingDTO()
        while 1:
            menu = input('0 Exit  1 CREATE DF  2 DEL NONE\n'
                         '>> ')
            if menu == '0':
                break
            elif menu == '1':
                dto.dframe = util.new_model('housing')
                HousingApi.print_this(dto.dframe)
            # elif menu == '2':
            #     util.remove_none_in_gugun(dto.dframe)
            else:
                continue


HousingApi.main()
