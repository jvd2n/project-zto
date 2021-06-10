from crime.services import CrimeService
from crime.models import CrimeDTO


class CrimeApi(object):

    @staticmethod
    def main():
        util = CrimeService()
        dto = CrimeDTO()
        dto_array = []
        while 1:
            menu = input('[1] CREATE DF from csv\n'
                         '[2] CREATE DF from xls\n'
                         '[3] Print All DataFrame\n'
                         '[0] EXIT\n'
                         '>> ')
            if menu == '0':
                break
            elif menu == '1':
                dto.dframe = util.new_model_from_csv('cctv_in_seoul.csv')
                dto_array.append(dto.dframe)
                dto.dframe = util.new_model_from_csv('crime_in_seoul.csv')
                dto_array.append(dto.dframe)
                dto.dframe = util.new_model_from_csv('police_position.csv')
                dto_array.append(dto.dframe)
                dto.dframe = util.new_model_from_csv('us_unemployment.csv')
                dto_array.append(dto.dframe)
                # util.print_dframe(dto.dframe)
            elif menu == '2':
                dto.dframe = util.new_model_from_xls('pop_in_seoul.xls')
                dto_array.append(dto.dframe)
                # util.print_dframe(dto.dframe)
            elif menu == '3':
                for i in dto_array:
                    util.print_dframe(i)
                # print(dto_array)
            else:
                continue


CrimeApi.main()
