class Country(object):
    # Super Class

    name = 'Country Name'
    population = 'Population'
    capital = 'Capital'

    def show(self):
        print('Country Class\' Method')


class Korea(Country):
    # Sub Class

    def show_name(self):
        print(f'Country Name is {self.name}')


def main():
    k = Korea()
    k.name = 'KOREA'
    k.show_name()
    print(k.capital)
    print(k.name)


main()

