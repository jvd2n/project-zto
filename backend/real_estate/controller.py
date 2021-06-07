from real_estate.housing import Housing
from real_estate.dataset import Dataset


class Controller(object):

    @staticmethod
    def main():
        while 1:
            menu = input('0-Exit 1-Create Model 2-Create DF\n'
                         '>> ')
            if menu == '0':
                break
            elif menu == '1':
                housing = Housing()
                dataset = Dataset()
                dataset.housing = housing.new_model()
                Controller.print_this(dataset)
            else:
                continue

    @staticmethod
    def print_this(this):
        print('*' * 100)
        print(f'1. Housing 의 type\n {type(this.housing)}')
        print(f'2. Housing 의 column\n {this.housing.columns}')
        print(f'3. Housing 의 상위 5개 행\n {this.housing.head(5)}')
        print(f'4. Housing 의 null 의 개수\n {this.housing.isnull().sum()}')
        print('*' * 100)


Controller.main()
