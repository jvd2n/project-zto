import os
from crime.services import CrimeService
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


class CrimeApi(object):

    @staticmethod
    def main():
        crime_svc = CrimeService()
        while 1:
            menu = input('[1] Seoul CCTV DF\n'
                         '[2] Seoul Crime DF\n'
                         '[3] PoliceStation DF\n'
                         '[4] Unemployment DF\n'
                         '[5] POP Seoul DF\n'
                         '[0] EXIT\n'
                         '>> ')
            if menu == '0':
                break
            elif menu == '1':
                crime_svc.csv({'context': './data/', 'fname': 'cctv_in_seoul'})
            elif menu == '2':
                crime_svc.csv({'context': './data/', 'fname': 'crime_in_seoul'})
            elif menu == '3':
                crime_svc.csv({'context': './data/', 'fname': 'police_position'})
            elif menu == '4':
                crime_svc.csv({'context': './data/', 'fname': 'us_unemployment'})
            elif menu == '5':
                crime_svc.xls({'context': './data/', 'fname': 'pop_in_seoul'})
            else:
                continue


CrimeApi.main()
