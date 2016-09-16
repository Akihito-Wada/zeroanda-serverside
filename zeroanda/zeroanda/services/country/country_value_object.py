class CountryVO:
    __index             = 0
    __coutnry_name    = None
    __abbreviation    = None
    __currency        = None
    __instrument      = None

    def __init__(self, index, country_name, abbreviation, currency):
        self.__index            = index
        self.__coutnry_name   = country_name
        self.__abbreviation   = abbreviation
        self.__currency       = currency

    @property
    def index(self):
        return self.__index

    @property
    def country_name(self):
        return self.__coutnry_name

    @property
    def abbreviation(self):
        return self.__abbreviation

    @property
    def currency(self):
        return self.__currency

    def __str__(self):
        return "name: {name} ({abbreviation}), currency: {currency}".format(name=self.country_name, abbreviation=self.abbreviation, currency=self.currency)