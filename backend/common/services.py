class CommonService(object):

    @staticmethod
    def print_dframe(this):
        print('*' * 100)
        print(f'1. Target 의 type\n {type(this)}')
        print(f'2. Target 의 column\n {this.columns}')
        print(f'3. Target 의 상위 5개 행\n {this.head()}')
        print(f'4. Target 의 null 의 개수\n {this.isnull().sum()}')
        print('*' * 100)